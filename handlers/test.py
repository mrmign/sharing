#encoding=utf-8

from base import BaseHandler
class TestHandler(BaseHandler):
    def get(self,prepage):
        print prepage
        # self.redirect(prepage)
