#!/usr/bin/env python
#coding=utf-8

from .base import BaseHandler
from models.database import LinkGroup

class HomeHandler(BaseHandler):
    def get(self):
        #self.write("hello")
        groups = self.db.find(LinkGroup)
        # for group in groups:
        # 	self.write(group.group_name)
        self.render(
                "main.html",
                groups=groups,
                )
