#coding=utf-8

from storm.expr import (Desc,Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import (User, LinkGroup,Link,FollowingUser,FollowingGroup)


class FollowUserHandler(BaseHandler):
    def get(self,user_id):
        following_user = FollowingUser()
        following_user.user_id = self.current_user.id
        following_user.follower_id = int(user_id)
        self.db.add(following_user)
        self.db.commit()
        follower_id = Select(FollowingUser.follower_id, FollowingUser.user_id==self.current_user.id)
        staffs = self.db.find(User,Not(User.id.is_in(follower_id)),User.id!=self.current_user.id)
        self.render("staff_picks.html",staffs=staffs,user=self.current_user)


class FollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        print group_id
        group_id = Select(FollowingGroup.group_id, FollowingGroup.user_id==self.current_user.id)
        groups = self.db.find(LinkGroup, Not(LinkGroup.id.is_in(group_id)),User.id!=self.current_user.id)
        self.render("popular_groups.html",groups=groups,user=self.current_user)
