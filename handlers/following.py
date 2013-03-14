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
        self.redirect(self.previous)


class FollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        self.redirect(self.previous) 

class UnfollowUserHandler(BaseHandler):
    def get(self,user_id):
        following_user=self.db.find(FollowingUser, FollowingUser.follower_id==int(user_id),\
                        FollowingUser.user_id==self.current_user.id).one()       
        self.db.remove(following_user)        
        self.redirect(self.previous)


class UnfollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group=self.db.find(FollowingGroup, FollowingGroup.group_id==int(group_id),\
                        FollowingGroup.user_id==self.current_user.id).one()       
        self.db.remove(following_group)        
        self.redirect(self.previous)


