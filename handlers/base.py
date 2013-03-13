#coding=utf-8

import logging
import tornado.web
from tornado.escape import url_escape, url_unescape

from models.database import User

logger = logging.getLogger('share' + __name__)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("share_user")
        # print "user-id from cookie", user_id
        if not user_id:
            return None
        return self.db.get(User,int(user_id))

    def initialize(self):
        # print self.request.uri
        if self.get_secure_cookie("common_previous"):
            self.previous = url_unescape(self.get_secure_cookie("common_previous"))
        else:
            self.previous = "/"
        self.set_secure_cookie("common_previous",str(url_escape(self.request.uri)))

   