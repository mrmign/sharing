"""The util class is to redirect to the 
previous page.
"""

# encoding=utf-8

from tornado.escape import url_unescape
from base import BaseHandler


class RedirectPageHandler(BaseHandler):
    def get(self):
        """Get previous page from cookie, then redirect to that"""
        pre = self.get_secure_cookie("previous")
        self.redirect(url_unescape(pre))
