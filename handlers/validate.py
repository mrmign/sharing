#coding=utf-8

from .base import BaseHandler
from models.database import User
from storm.store import *

class ValidateHandler(BaseHandler):
    def get(self):
        username=self.get_argument('username')
        email=self.get_argument('email')
        password=self.get_argument('password')

        user1=self.db.find(User,User.username==username).one()
        user2=self.db.find(User,User.email==email).one()


        if not user1 and not user2:
            user=User()
            user.username=username
            user.email=email
            user.password=password
            self.db.add(user)
            self.db.commit()
            self.render("login.html" , login_msg=" signup successfully,please login!")

        else:
            self.render("signup.html")

    def post(self):
        username=self.get_argument('username')
        password=self.get_argument('password')
        user = self.db.find(User,User.username==username, User.password==password).one()
        
        if user:
            self.render(
                "me.html",user=user
                )
        else:
            self.render(
                "login.html" ,login_msg="your username or password is wrong,please print again"                
                )
        
        

