#encoding=utf-8

import json
from storm.expr import (Desc,Asc, Select, Not)

from .base import BaseHandler
from models.database import User,FollowingUser, LinkGroup, Link
from settings import NUM_FEED
"""
request type  | identyfier
feed          |     1

return status | identifier
OK                 200
NO MORE            404
"""
class LoadMoreHandler(BaseHandler):
    def post(self):
        request_type = self.get_argument("type")
        page = self.get_argument("page_num")
        result, cnt, total_page = {
                "1": self._get_more_feed(int(page)),
        }.get(request_type, "There is nothing to be loaded.")

        ret = {"ret":result, "cnt":cnt, "total":total_page}
        self.write(json.dumps(ret))

    def _get_more_feed(self, page):
        follower_id = Select(FollowingUser.follower_id,(FollowingUser.user_id==self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        links = self.db.find(Link, Link.group_id.is_in(group_id)).order_by(Desc(Link.updated))
        total = links.count()
        total_page = (total - 1) / NUM_FEED + 1
        l = links[10*(page - 1): 10*page]
        
        return self.render_string("modules/more_feed.html",links=l, ret_count=links.count(), total_page=total_page), links.count(), total_page
