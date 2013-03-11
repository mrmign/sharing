#encoding=utf-8

from base import BaseHandler
from models.database import Link

class LinkSaveHandler(BaseHandler):
    def get(self,**link_url):
        # link_url = self.get_argument("url", None)
        print link_url["link"]
