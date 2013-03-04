#coding=utf-8

import tornado.web
from .base import BaseHandler
from models.database import User


class SignupHandler(BaseHandler):
	def get(self):
		self.render("signup.html")
	def post(self):
		username=self.get_argument('username')
		email=self.get_argument('email')
		password=self.get_argument('password')
		user=User()
		user.username=username
		user.email=email
		user.password=password
		self.db.add(user)
		self.db.commit()
		self.render("login.html",login_msg="sign up successfully, please login")