# encoding=utf-8
import json

from storm.expr import (Desc, Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup, Link, FollowingUser, FollowingGroup, Comment


class TestHandler(BaseHandler):
    def get(self):
        # print prepage
        # self.redirect(prepage)
        self.render("test.html")

    def post(self):
        print self.get_argument("type")
        print self.get_argument("page_num")
        # self.write("hello, Nice to meet your.")

        page = int(self.get_argument("page_num"))
        follower_id = Select(FollowingUser.follower_id, (
            FollowingUser.user_id == self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        links = self.db.find(Link, Link.group_id.is_in(
            group_id)).order_by(Desc(Link.created))[10*(page - 1): 10*page]
        out = self.render_string(
            "modules/more_feed.html", links=links, ret_count=links.count())

        result = {"html_data": out, "cnt": 10}
        self.write(json.dumps(result))
