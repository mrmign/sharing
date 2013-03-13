#coding=utf-8
from storm.expr import (Desc,Asc, Select, Not)
from .base import BaseHandler
from models.database import User,FollowingUser,FollowingGroup

class UserHandler(BaseHandler):
    def get(self,user_id):       
        if self.current_user:
            userid = Select(FollowingUser.user_id,(FollowingUser.follower_id==self.current_user.id))        
            users = self.db.find(User, User.id.is_in(userid))       
            u = self.db.get(User,int(user_id))
            self.render("other_user.html",users=users,u=u,groups=u.groups,description=u.introduction,user=self.current_user)
        else:
            u = self.db.get(User,int(user_id))
            self.render("home_user.html",user=u,groups=u.groups,description=u.introduction)
            
