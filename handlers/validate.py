#!/usr/bin/env python
#coding=utf-8

from .base import BaseHandler
from models.database import User
from storm.store import *

class ValidateHandler(BaseHandler):
    def post(self):
        username=self.get_argument('username')
        password=self.get_argument('password')
        user = self.db.find(User,User.username==username, User.password==password).one()
        
        if user:
            self.render(
                "app.html",user=user
                )
        else:
            self.render(
                "login.html" ,login_msg="your username or password is wrong,please print again"                
                )
        
        

