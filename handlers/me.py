#coding=utf-8

from storm.expr import (Desc,Asc, Select)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup,Link


class FeedHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        self.render("feed.html",user=self.current_user)

class MyLinksHandler(BaseHandler):
    def get(self):
        sub = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Link.group_id.is_in(sub)).order_by(Desc(Link.created))
            
        #     print self.current_user.id, self.current_user.username
        self.render("mylinks.html",links=links,user=self.current_user)
    
