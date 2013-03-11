#encoding=utf-8

import tornado.web

from base import BaseHandler
from models.database import Link

class LinkSaveHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self,link_id):
        link = self.db.get(Link, int(link_id))
        print link.title
