#coding:utf-8
import tornado.web

from storm.locals import AutoReload
from base import BaseHandler
from models.database import LinkGroup

class GroupHandler(BaseHandler):
	def get(self, group_id):
		group = self.db.get(LinkGroup, int(group_id))
		if self.current_user:
		    self.render("group_logined.html",group=group,user=self.current_user)
		else:		
		    self.render("group.html",group=group)

