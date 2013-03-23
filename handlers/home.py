# coding=utf-8
from storm.expr import (Desc, Asc, Select, Not)
from .base import BaseHandler
from models.database import LinkGroup, FollowingGroup, User


class HomeHandler(BaseHandler):
    def get(self):
        groups = self.db.find(LinkGroup, LinkGroup.private == 0).order_by(
            Desc(LinkGroup.follower_count))
        if self.current_user:
            self.render("home_popular_logined.html",
                        user=self.current_user, groups=groups,)
        else:
            self.render("home_popular.html", groups=groups,)


class HomeRecentHandler(BaseHandler):
    def get(self):
        follow_groups = self.db.find(FollowingGroup).group_by(
            FollowingGroup.group_id).order_by(Desc(FollowingGroup.id))
        follow_ids = [g.group_id for g in follow_groups]
        groups = self.db.find(LinkGroup, LinkGroup.id.is_in(
            follow_ids), LinkGroup.private == 0)
        if self.current_user:
            self.render("home_recent_logined.html",
                        user=self.current_user, groups=groups,)
        else:
            self.render("home_recent.html", groups=groups,)
