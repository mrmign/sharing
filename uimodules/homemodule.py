# coding=utf-8

import tornado.web

class HomeListModule(tornado.web.UIModule):
	def render(self, group):
		return self.render_string("modules/homelist.html", group=group)