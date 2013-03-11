#coding:utf-8

from storm.locals import AutoReload
from base import BaseHandler
from models.database import LinkGroup

class GroupHandler(BaseHandler):
	def get(self, group_id):
		group = self.db.get(LinkGroup, int(group_id))
		self.render("group.html",group=group)

class GroupLoginedHandler(BaseHandler):
	def get(self, group_id):
		group = self.db.get(LinkGroup, int(group_id))
		self.render("group_logined.html",group=group,user=self.current_user)