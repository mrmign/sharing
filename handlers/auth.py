#coding=utf-8

import tornado.web
from base import BaseHandler

from models.database import User


class LoginHandler(BaseHandler):
    def get(self):
        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        self.render("login.html",login_msg=" ")

    def post(self):
        username=self.get_argument('username')
        password=self.get_argument('password')
        user = self.db.find(User,User.username==username, User.password==password).one()
        
        if user:
            self.set_secure_cookie("share_user", str(user.id))
            self.render("me.html",user=user)
            
        else:
            self.render(
                "login.html" ,login_msg="your username or password is wrong,please print again"                
                )


class SignupHandler(BaseHandler):
    def get(self):
        self.render("signup.html", signup_msg="")

    def post(self):
        username = self.get_argument('username')
        email = self.get_argument("email")
        password = self.get_argument("password")
        # print username, email, password
        user1 = self.db.find(User,User.username==username).one()
        user2 = self.db.find(User,User.email==email).one()
        # print user1e
        if not user1 and not user2:
            user = User()
            user.username = username
            user.email = email
            user.password = password 
            self.db.add(user)
            self.db.commit()
            self.render("login.html", login_msg="signup successfully,please login!")
        else:
            self.render("signup.html", signup_msg="your username or email has existed,please print again")

class LogoutHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.clear_cookie("share_user")
        self.redirect("/")
