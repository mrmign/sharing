"""BaseHandler for all the handlers. Defines functions
that all the handlers may use.
1. get the db connection
2. get current user
3. do initialization before handling the request.
"""

# coding=utf-8

import logging
import tornado.web
from tornado.escape import url_escape, url_unescape

from models.database import User

logger = logging.getLogger('share' + __name__)


class BaseHandler(tornado.web.RequestHandler):
    
    @property
    def db(self):
        """Return db connection as a property."""
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("share_user")
        # print "user-id from cookie", user_id
        if not user_id:
            return None
        return self.db.get(User, int(user_id))
           
    def initialize(self):
        """Set the previous request uri, and update it.
        if the request is from extension or loadmore request, 
        it will do nothing.
        """ 

        # load more changes the previous uri, it will cause like handler not working
        # import pdb
        # pdb.set_trace()
        if self.request.uri.find("loadmore") == 1 or self.request.uri.find("extension") == 1:
            return
        # print self.request.uri

        if self.get_secure_cookie("common_previous"):
            self.previous = url_unescape(
                self.get_secure_cookie("common_previous"))
        else:
            self.previous = "/"

        self.set_secure_cookie("common_previous", str(
                        url_escape(self.request.uri)))
