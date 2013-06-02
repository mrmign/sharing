"""Loadmore class to load more links.

According different request type, return 
different links. The following is the type.

request type     | identyfier
feed             |     1
mylink           |     2
me recentlinks   |     3

return status    | identifier
OK                 200
NO MORE            202
"""

# encoding=utf-8

import json
from storm.expr import (Desc, Asc, Select, Not)

from .base import BaseHandler
from models.database import User, FollowingUser, LinkGroup, Link
from settings import NUM_FEED, NUM_RECENT_LINKS



class LoadMoreHandler(BaseHandler):
    def post(self):
        """Get the request type, call different 
        functions according to the identifier.
        """
        request_type = self.get_argument("type")
        page = self.get_argument("page_num")
        if request_type == "1":
            result, status_code = self._get_more_feed(int(page))
        elif request_type == "2":
            result, status_code = self._get_more_mylink(int(page))
        elif request_type == "3":
            result, status_code = self._get_more_recent_links(int(page))
        # result, status_code = {
        #         "1": self._get_more_feed(int(page)),
        #         "2": self._get_more_mylink(int(page)),
        # }.get(request_type, "There is nothing to be loaded.")

        ret = {"ret": result, "status_code": status_code}
        self.write(json.dumps(ret))

    def _get_more_feed(self, page):
        """Get more links in the feed catagory."""
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        links = self.db.find(Link, Link.group_id.is_in(
            group_id)).order_by(Desc(Link.updated))
        total = links.count()
        total_page = (total - 1) / NUM_FEED + 1
        l = links[NUM_FEED*(page - 1): NUM_FEED*page]
        if page < total_page:
            status_code = 200
        else:
            status_code = 202
        return self.render_string("modules/more_feed.html", links=l, 
            groups=self.current_user.groups, ret_count=links.count()), status_code

    def _get_more_mylink(self, page):
        """Get more links of my own"""
        sub = Select(LinkGroup.id, (LinkGroup.user_id == self.current_user.id))
        links = self.db.find(Link, Link.group_id.is_in(
            sub)).order_by(Desc(Link.updated))
        mygroups = self.db.find(
            LinkGroup, LinkGroup.user_id == self.current_user.id)
        total = links.count()
        total_page = (total - 1) / NUM_FEED + 1
        l = links[NUM_FEED*(page - 1): NUM_FEED*page]
        if page <= total_page:
            status_code = 200
        else:
            status_code = 202
        return self.render_string("modules/more_mylinks.html", links=l, 
            groups=mygroups, ret_count=links.count()), status_code

    def _get_more_recent_links(self, page):
        """Get more recent links """
        group_id = Select(LinkGroup.id, (
            LinkGroup.user_id == self.current_user.id))
        links = self.db.find(Link, Not(Link.group_id.is_in(
            group_id))).order_by(Desc(Link.updated))
        total = links.count()
        total_page = (total - 1) / NUM_RECENT_LINKS + 1
        l = links[NUM_RECENT_LINKS*(page - 1): NUM_RECENT_LINKS*page]
        if page <= total_page:
            status_code = 200
        else:
            status_code = 202
        return self.render_string("modules/more_recent_links.html", links=l, 
            user=self.current_user), status_code
