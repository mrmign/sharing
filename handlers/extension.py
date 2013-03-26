# coding=utf-8

import json
from urlparse import urlparse
from base import BaseHandler
from models.database import LinkGroup, Link
class UserDataHandler(BaseHandler):
    def get(self):
        # print self.current_user.id
        self.write(json.dumps({"id":self.current_user.id}))


class UserGroupsHandler(BaseHandler):
    def get(self):
        groups = []
        for group in self.current_user.groups:
            groups.append({"id":group.id,"group_name":group.group_name})

        resp = {"objects":groups}

        self.write(json.dumps(resp))

class ExtensionAddLinkHandler(BaseHandler):
    def post(self):
        # import pdb
        # pdb.set_trace()
        link = Link()
        link.url =self.get_argument("url")
        link.domain = urlparse(link.url).netloc
        link.title = self.get_argument("title")
        link.description = self.get_argument("description", u'')

        if self.get_argument("new_list") == 'true':
            newgroup = LinkGroup()
            newgroup.user_id = self.current_user.id
            newgroup.group_name = self.get_argument("group_name")
            newgroup.private = 1 if self.get_argument("is_private")=="true" else 0
            newgroup.links_count = 1;
            self.db.add(newgroup)
            self.db.commit()
            link.group_id = newgroup.id
        else:
            group = self.get_argument("group")
            link.group_id = int(group)
            lg = self.db.get(LinkGroup, link.group_id)
            lg.links_count += 1

        self.db.add(link)
        self.db.commit()

      