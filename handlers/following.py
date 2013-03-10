#coding=utf-8

from storm.expr import (Desc,Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup,Link,Following


class FollowHandler(BaseHandler):
    def get(self,userid):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        
        following = Following()
        following.user_id = self.current_user.id
        following.follower_id = int(userid)
        self.db.add(following)
        self.db.commit()
        follower_id = Select(Following.follower_id, Following.user_id==self.current_user.id)
        staffs = self.db.find(User,Not(User.id.is_in(follower_id)),User.id!=self.current_user.id)
        self.render("staff_picks.html",staffs=staffs,user=self.current_user)
