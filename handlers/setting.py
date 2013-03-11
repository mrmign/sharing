#encoding=utf-8
from storm.expr import (Desc,Asc, Select, Not)
import tornado.web

from base import BaseHandler
from models.database import User

class ProfileHandler(BaseHandler):
	def get(self):
		print self.current_user
		introduction = self.current_user.introduction
		if not introduction:
			introduction="Add Description"
		self.render("profile.html" ,user=self.current_user ,groups=self.current_user.groups,description=introduction)

class SettingsProfileHandler(BaseHandler):
	def get(self):
		self.render("settings_profile.html" ,user=self.current_user)

	def post(self):
		introduction = self.get_argument('description')
		user = self.db.find(User,User.id==self.current_user.id).one()
		user.introduction = introduction
		self.db.commit()
		if not introduction:
			introduction = "Add Description"

		self.render("profile.html" ,user=self.current_user ,groups=self.current_user.groups,description=introduction)
