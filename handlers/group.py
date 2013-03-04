#coding:utf-8

from base import BaseHandler
from models.database import LinkGroup

class GroupHandler(BaseHandler):
	def get(self, groupid):
		group = self.db.get(LinkGroup, int(groupid))
		print groupid
		print group.group_name
		self.render("group.html",group=group)