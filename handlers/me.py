# encoding=utf-8

from storm.expr import (Desc, Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup, Link, FollowingUser, FollowingGroup, Comment
from settings import NUM_FEED
from tornado.escape import url_escape


class FeedHandler(BaseHandler):
    def get(self):
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        links = self.db.find(Link, Link.group_id.is_in(
            group_id)).order_by(Desc(Link.updated))
        self.render("feed.html", links=links[:10], user=self.current_user)


class MyLinksHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        sub = Select(LinkGroup.id, (LinkGroup.user_id == self.current_user.id))
        links = self.db.find(Link, Link.group_id.is_in(
            sub)).order_by(Desc(Link.updated))

        self.render("mylinks.html", links=links[:10], link_count=links.count(), user=self.current_user)


class MeGroupHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, groupid):
        group = self.db.get(LinkGroup, int(groupid))
        link_id = Select(Link.id, (Link.group_id == int(group.id)))
        links = self.db.find(Link, Link.id.is_in(
            link_id)).order_by(Desc(Link.updated))
        self.render("megroup.html", group=group,
                    user=self.current_user, links=links)


class FollowingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        users = self.db.find(User, User.id.is_in(follower_id))
        group_id = Select(FollowingGroup.group_id, (
            FollowingGroup.user_id == self.current_user.id))
        groups = self.db.find(LinkGroup, LinkGroup.id.is_in(group_id))
        self.render("following.html", groups=groups,
                    users=users, user=self.current_user)


class FollowerHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_id = Select(FollowingUser.user_id, (
            FollowingUser.follower_id == self.current_user.id))
        users = self.db.find(User, User.id.is_in(user_id))
        self.render("follower.html", users=users, user=self.current_user)


class MeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("me.html", user=self.current_user)
