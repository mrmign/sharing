"""User's profile.

1. User's basic info
2. Edit user's profile
3. User's account setting.
"""

# encoding=utf-8
from storm.expr import (Desc, Asc, Select, Not)
import tornado.web

from base import BaseHandler
from models.database import User, FollowingUser, FollowingGroup


class ProfileHandler(BaseHandler):
    def get(self):
        """user's basic infomation"""
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        followings = self.db.find(User, User.id.is_in(follower_id))
        follower = Select(FollowingUser.user_id, (
            FollowingUser.follower_id == self.current_user.id))
        followers = self.db.find(User, User.id.is_in(follower))
        introduction = self.current_user.introduction
        if not introduction:
            introduction = "Add Description"
        self.render(
            "profile.html", user=self.current_user, followers=followers,
            followings=followings, groups=self.current_user.groups, description=introduction)


class SettingsProfileHandler(BaseHandler):
    def get(self):
        self.render("settings_profile.html", user=self.current_user)

    def post(self):
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        followings = self.db.find(User, User.id.is_in(follower_id))
        follower = Select(FollowingUser.user_id, (
            FollowingUser.follower_id == self.current_user.id))
        followers = self.db.find(User, User.id.is_in(follower))
        introduction = self.get_argument('description')
        user = self.db.find(User, User.id == self.current_user.id).one()
        user.introduction = introduction
        self.db.commit()
        if not introduction:
            introduction = "Add Description"

        self.render(
            "profile.html", user=self.current_user, followers=followers,
            followings=followings, groups=self.current_user.groups, description=introduction)


class SettingsAccountHandler(BaseHandler):
    """User's account setting operation."""
    def get(self):
        self.render("settings_account.html", user=self.current_user)

    def post(self):
        username = self.get_argument('username')
        email = self.get_argument('email')
        password = self.get_argument('password1')
        user = self.db.find(User, User.id == self.current_user.id).one()
        user.username = username
        user.email = email
        if password:
            user.password = password
        self.db.commit()
        self.render("settings_account.html", user=self.current_user)