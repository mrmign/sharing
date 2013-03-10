#coding=utf-8

from storm.expr import (Desc,Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup,Link,Following


class FeedHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        follower_id = Select(Following.follower_id,(Following.user_id==self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id==follower_id))
        links = self.db.find(Link, Link.group_id.is_in(group_id)).order_by(Desc(Link.created))
        self.render("feed.html",links=links,user=self.current_user)

class MyLinksHandler(BaseHandler):
    def get(self):
        sub = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Link.group_id.is_in(sub)).order_by(Desc(Link.created))
            
        #     print self.current_user.id, self.current_user.username
        self.render("mylinks.html",links=links,user=self.current_user)
    
class MeGroupHandler(BaseHandler):
    def get(self, groupid):
        group = self.db.get(LinkGroup, int(groupid))
        # print group.links.count()
        # print group.group_name
        # for l in group.links:
        #     print l.id
        # group = AutoReload
        self.render("megroup.html",group=group,user=self.current_user)

class StaffPicksHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        staffs = self.db.find(User,User.id!=self.current_user.id)
        self.render("staff_picks.html",staffs=staffs,user=self.current_user)

class PopularGroupsHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        group_id = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        groups = self.db.find(LinkGroup, Not(LinkGroup.id.is_in(group_id)))
        self.render("popular_groups.html",groups=groups,user=self.current_user)

class RecentLinksHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        group_id = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Not(Link.group_id.is_in(group_id))).order_by(Desc(Link.created))
        self.render("recent_links.html",links=links,user=self.current_user)

class NewGroupHandler(BaseHandler):
    def get(self):
        self.render("newgroup.html", user = self.current_user,newgroup_msg="")

    def post(self):
        group_name = self.get_argument('group_name')
        group = self.db.find(LinkGroup,LinkGroup.user_id==self.current_user.id,LinkGroup.group_name==group_name).one()
        if not group:
            newgroup=LinkGroup()
            newgroup.user_id=self.current_user.id
            newgroup.group_name=group_name
            self.db.add(newgroup)
            self.db.commit()
            self.render("me.html",user=self.current_user)
        else:
            self.render("newgroup.html",user=self.current_user,newgroup_msg="your group_name has existed,please try again")