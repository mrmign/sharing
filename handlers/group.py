"""Classes related to group.
Add, delete, edit group. 
"""

# coding:utf-8
from storm.expr import (Desc, Asc, Select, Not)
import tornado.web

from storm.locals import AutoReload
from base import BaseHandler
from models.database import User, LinkGroup, Link, FollowingUser, FollowingGroup, Comment
from settings import NUM_FEED
from tornado.escape import url_escape


class GroupHandler(BaseHandler):
    def get(self, group_id):
        group = self.db.get(LinkGroup, int(group_id))
        if self.current_user:
            self.render(
                "group_logined.html", group=group, user=self.current_user)
        else:
            self.render("group.html", group=group)


class AddGroupHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        """Return group form to fillin."""
        self.render("addgroup.html", user=self.current_user, newgroup_msg="")

    @tornado.web.authenticated
    def post(self):
        """Add new group to database"""
        group_name = self.get_argument('groupname')
        group_description = self.get_argument('group_description', u'')
        group = self.db.find(
            LinkGroup,LinkGroup.user_id==self.current_user.id,
            LinkGroup.group_name==group_name).one()
        if not group:
            newgroup=LinkGroup()
            newgroup.user_id=self.current_user.id
            newgroup.group_name=group_name
            newgroup.description=group_description
            radio_value = self.get_argument('list-sharing')
            if radio_value == "private":
                newgroup.private = 1
            self.db.add(newgroup)
            self.db.commit()
            self.render("me.html", user=self.current_user)
        else:
            self.render("addgroup.html", user=self.current_user,
                        newgroup_msg="your group_name has existed,please try again")


class DeleteGroupHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, group_id):
        """Delete the group, and comments and likes related to it."""
        link_id = Select(Link.id, (Link.group_id == int(group_id)))
        links = self.db.find(Link, Link.id.is_in(link_id))
        for link in links:            
            for comment in link.comments:
                self.db.remove(comment)
            for like in link.likes:
                self.db.remove(like)
            self.db.remove(link)
        group = self.db.find(LinkGroup, LinkGroup.id == int(group_id)).one()
        self.db.remove(group)
        self.db.commit()
        self.render("me.html", user=self.current_user)


class EditGroupHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, group_id, previous_page):
        """Get group's info"""
        self.set_secure_cookie("previous", url_escape(previous_page))
        group = self.db.find(LinkGroup, LinkGroup.id == int(group_id)).one()
        self.render("editgroup.html", user=self.current_user,
                    group_name=group.group_name, group=group)

    @tornado.web.authenticated
    def post(self, group_id, previous_page):
        """Update group's info"""
        group_name = self.get_argument('groupname')
        group_description = self.get_argument('group_description', u'')
        group = self.db.find(LinkGroup,LinkGroup.id==int(group_id)).one()
        group.group_name = group_name
        group.description=group_description
        radio_value = self.get_argument('list-sharing')
        if radio_value == "private":
            group.private = 1
        else:
            group.private = 0
        self.db.commit()
        self.redirect(previous_page)
