#coding:utf-8

from storm.locals import AutoReload
from base import BaseHandler
from models.database import LinkGroup

class GroupHandler(BaseHandler):
	def get(self, groupid):
		group = self.db.get(LinkGroup, int(groupid))
		# print groupid
		# print group.group_name
		self.render("group.html",group=group)

class MeGroupHandler(BaseHandler):
	def get(self, groupid):
		group = self.db.get(LinkGroup, int(groupid))
		print group.links.count()
		print group.group_name
		# group = AutoReload
		self.render("megroup.html",group=group,user=self.current_user)