#coding=utf-8

import logging
import tornado.web

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
