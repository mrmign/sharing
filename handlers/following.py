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
        # self.redirect("/me/staff_picks")
        self.redirect(self.previous)


class FollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        self.redirect(self.previous)
        

class FollowerFollowUserHandler(BaseHandler):
    def get(self,user_id):
        following_user = FollowingUser()
        following_user.user_id = self.current_user.id
        following_user.follower_id = int(user_id)
        self.db.add(following_user)
        self.db.commit()
        self.redirect("/me/follower")

class FollowerUnfollowUserHandler(BaseHandler):
    def get(self,user_id):
        following_user=self.db.find(FollowingUser, FollowingUser.follower_id==int(user_id),\
                        FollowingUser.user_id==self.current_user.id).one()       
        self.db.remove(following_user)        
        self.redirect("/me/follower")

class FollowingUnfollowUserHandler(BaseHandler):
    def get(self,user_id):
        following_user=self.db.find(FollowingUser, FollowingUser.follower_id==int(user_id),\
                        FollowingUser.user_id==self.current_user.id).one()       
        self.db.remove(following_user)        
        self.redirect("/me/following")

class FollowingUnfollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group=self.db.find(FollowingGroup, FollowingGroup.group_id==int(group_id),\
                        FollowingGroup.user_id==self.current_user.id).one()       
        self.db.remove(following_group)        
        self.redirect("/me/following")

class GroupFollowGroupHandler(BaseHandler):
    def get(self, group_id):
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        self.redirect("/group/logined/{0}".format(group_id))

class GroupUnfollowGroupHandler(BaseHandler):
    def get(self,group_id):
        following_group=self.db.find(FollowingGroup, FollowingGroup.group_id==int(group_id),\
                        FollowingGroup.user_id==self.current_user.id).one()       
        self.db.remove(following_group)        
        self.redirect("/group/logined/{0}".format(group_id))

class UserFollowGroupHandler(BaseHandler):
    def get(self, group_id):
        group = self.db.get(LinkGroup,int(group_id))
        following_group = FollowingGroup()
        following_group.user_id = self.current_user.id
        following_group.group_id = int(group_id)
        self.db.add(following_group)
        self.db.commit()
        self.redirect("/user/{0}".format(group.user.id))

class UserUnfollowGroupHandler(BaseHandler):
    def get(self,group_id):
        group = self.db.get(LinkGroup,int(group_id))
        following_group=self.db.find(FollowingGroup, FollowingGroup.group_id==int(group_id),\
                        FollowingGroup.user_id==self.current_user.id).one()       
        self.db.remove(following_group)        
        self.redirect("/user/{0}".format(group.user.id))

            
class UserFollowUserHandler(BaseHandler):
    def get(self,user_id):        
        following_user = FollowingUser()
        following_user.user_id = self.current_user.id
        following_user.follower_id = int(user_id)
        self.db.add(following_user)
        self.db.commit()
        self.redirect("/user/{0}".format(user_id))

class UserUnfollowUserHandler(BaseHandler):
    def get(self, user_id):
        following_user=self.db.find(FollowingUser, FollowingUser.follower_id==int(user_id),\
                        FollowingUser.user_id==self.current_user.id)[0]       
        self.db.remove(following_user)        
        self.redirect("/user/{0}".format(user_id))
