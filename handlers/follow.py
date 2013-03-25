# coding=utf-8

from storm.expr import (Desc, Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import (
    User, LinkGroup, Link, FollowingUser, FollowingGroup)


class FollowUserHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, user_id):
        u = self.db.get(User, int(user_id))
        u.follower_count += 1
        following_user = FollowingUser()
        following_user.user_id = self.current_user.id
        following_user.follower_id = int(user_id)
        self.db.add(following_user)
        self.db.commit()
        self.redirect(self.previous)


class FollowGroupHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, group_id):
        group = self.db.get(LinkGroup, int(group_id))
        group.follower_count += 1
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        self.redirect(self.previous)


class UnfollowUserHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, user_id):
        u = self.db.get(User, int(user_id))
        u.follower_count -= 1
        following_user = self.db.find(
            FollowingUser, FollowingUser.follower_id == int(user_id),
            FollowingUser.user_id == self.current_user.id).one()
        self.db.remove(following_user)
        self.db.commit()
        self.redirect(self.previous)


class UnfollowGroupHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, group_id):
        following_group = self.db.find(
            FollowingGroup, FollowingGroup.group_id == int(group_id),
            FollowingGroup.user_id == self.current_user.id).one()
        group = self.db.get(LinkGroup, int(group_id))
        group.follower_count -= 1
        self.db.remove(following_group)
        self.db.commit()
        self.redirect(self.previous)
