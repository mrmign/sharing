#coding=utf-8

from .base import BaseHandler
from models.database import LinkGroup

class HomeHandler(BaseHandler):
    def get(self):
        groups = self.db.find(LinkGroup)
        if self.current_user:
            self.render("home_popular_logined.html",user=self.current_user,groups=groups,)
        else:            
            self.render("home_popular.html",groups=groups,)

class HomeRecentHandler(BaseHandler):
    def get(self):
        groups = self.db.find(LinkGroup)
        if self.current_user:
            self.render("home_recent_logined.html",user=self.current_user,groups=groups,)
        else:
            self.render("home_recent.html",groups=groups,)
            
