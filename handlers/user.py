#coding=utf-8
from storm.expr import (Desc,Asc, Select, Not)
from .base import BaseHandler
from models.database import User,FollowingUser,FollowingGroup

class UserHandler(BaseHandler):
    def get(self,user_id): 
        u=self.db.get(User,int(user_id)) 
        print user_id, u.id     
        if self.current_user:
            follower_id = Select(FollowingUser.follower_id,FollowingUser.user_id==int(user_id))
            followings = self.db.find(User, User.id.is_in(follower_id))
            follower = Select(FollowingUser.user_id,(FollowingUser.follower_id==int(user_id)))
            followers = self.db.find(User, User.id.is_in(follower))              
            self.render("other_user.html",followings=followings,followers=followings,groups=u.groups,u=u,user=self.current_user)

        else:
            
            self.render("home_user.html",user=u,groups=u.groups,description=u.introduction)
            
