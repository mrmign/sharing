#encoding=utf-8

import json
from tornado.template import Template

from base import BaseHandler
"""
request type  | identyfier
feed          |     1


"""
class LoadMoreHandler(BaseHandler):
    def post(self):
        print "request"
        request_type = self.get_argument("type")
        page = self.get_argument("page_num")
        result, cnt = {
                "1": self._get_more_feed(int(page)),
        }.get(request_type, "There is nothing to be loaded.")

        ret = {"ret":result, "cnt":cnt}
        print ret
        self.write(json.dumps(ret))

    def _get_more_feed(self, page):
        follower_id = Select(FollowingUser.follower_id,(FollowingUser.user_id==self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        links = self.db.find(Link, Link.group_id.is_in(group_id)).order_by(Desc(Link.created))[10*(page - 1): 10*page]
        
        return self.render_string("modules/more_feed.html",links=links, ret_count=links.count()), links.count()
