#encoding=utf-8

import tornado.web

from base import BaseHandler
from models.database import Link,LinkGroup

class LinkSaveHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self,group_id, link_id):

        l = self.db.get(Link,int(link_id))
        group = self.db.get(LinkGroup, l.group_id)
        link = Link()
        link.title = l.title
        link.url = l.url
        link.url_domain = l.url_domain      
        link.group_id = int(group_id)
        self.db.add(link)
        self.db.commit()
        
        self.render("group_logined.html",group=group,user=self.current_user)
        
