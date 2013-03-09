#coding=utf-8

from .base import BaseHandler
from models.database import LinkGroup

class HomeHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.render("me.html",user=self.current_user)
        else:
            groups = self.db.find(LinkGroup)
            self.render(
                    "main.html",
                    groups=groups,
                    )
            
