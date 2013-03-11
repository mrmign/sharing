#coding=utf-8

from storm.expr import (Desc,Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup,Link,FollowingUser,FollowingGroup




class FeedHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        follower_id = Select(Following.follower_id,(Following.user_id==self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
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
        follower_id = Select(FollowingUser.follower_id, FollowingUser.user_id==self.current_user.id)
        staffs = self.db.find(User,Not(User.id.is_in(follower_id)),User.id!=self.current_user.id)
        self.render("staff_picks.html",staffs=staffs,user=self.current_user)

class PopularGroupsHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        group_id = Select(FollowingGroup.group_id, FollowingGroup.user_id==self.current_user.id)
        groups = self.db.find(LinkGroup, Not(LinkGroup.id.is_in(group_id)),User.id!=self.current_user.id)
        self.render("popular_groups.html",groups=groups,user=self.current_user)

class RecentLinksHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        group_id = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Not(Link.group_id.is_in(group_id))).order_by(Desc(Link.created))
        self.render("recent_links.html",links=links,user=self.current_user)

class FollowingHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        # follower_id = Select(Following.follower_id,(Following.user_id==self.current_user.id))
        # group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))
        # links = self.db.find(Link, Link.group_id.is_in(group_id)).order_by(Desc(Link.created))
        follower_id = Select(FollowingUser.follower_id,(FollowingUser.user_id==self.current_user.id))
        users = self.db.find(User, User.id.is_in(follower_id))
        self.render("following.html",users=users,user=self.current_user)

class FollowerHandler(BaseHandler):
    def get(self):

        # if self.current_user:
        #     print self.current_user.id, self.current_user.username
        user_id = Select(FollowingUser.user_id,(FollowingUser.follower_id==self.current_user.id))        
        users = self.db.find(User, User.id.is_in(user_id))
        self.render("following.html",users=users,user=self.current_user)