"""Recommendation of pelple, group, links.
"""

# encoding=utf-8

from storm.expr import (Desc, Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup, Link, FollowingUser, FollowingGroup, Comment
from settings import NUM_FEED
from tornado.escape import url_escape


class StaffPicksHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        """Recommend the popular people """
        follower_id = Select(
            FollowingUser.follower_id, FollowingUser.user_id == self.current_user.id)
        staffs = self.db.find(User, Not(User.id.is_in(
            follower_id)), User.id != self.current_user.id).order_by(Desc(User.follower_count))[:16]
        self.render("staff_picks.html", staffs=staffs, user=self.current_user)


class PopularGroupsHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        group_id = Select(
            FollowingGroup.group_id, FollowingGroup.user_id == self.current_user.id)
        group_id2 = Select(
            LinkGroup.id, LinkGroup.user_id == self.current_user.id)
        groups = self.db.find(LinkGroup, Not(LinkGroup.id.is_in(group_id)), Not(LinkGroup.id.is_in(
            group_id2)), LinkGroup.private == 0).order_by(Desc(LinkGroup.follower_count))[:12]
        self.render("popular_groups.html",
                    groups=groups, user=self.current_user)


class RecentLinksHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        """Recommend the recent links"""
        group_id = Select(LinkGroup.id, (
            LinkGroup.user_id == self.current_user.id))
        links = self.db.find(Link, Not(Link.group_id.is_in(
            group_id))).order_by(Desc(Link.updated))[0:15]
        # print links.count()
        self.render("recent_links.html", links=links, user=self.current_user)