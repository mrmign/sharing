#coding=utf-8

from storm.expr import (Desc,Asc, Select, Not)
import tornado.web
from base import BaseHandler

from models.database import User, LinkGroup,Link,FollowingUser,FollowingGroup,Comment

class FeedHandler(BaseHandler):
    def get(self):
        follower_id = Select(FollowingUser.follower_id,(FollowingUser.user_id==self.current_user.id))
        group_id = Select(LinkGroup.id, (LinkGroup.user_id.is_in(follower_id)))

        links = self.db.find(Link, Link.group_id.is_in(group_id)).order_by(Desc(Link.created))
        self.render("feed.html",links=links[:10],user=self.current_user)

class MyLinksHandler(BaseHandler):
    def get(self):
        sub = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Link.group_id.is_in(sub)).order_by(Desc(Link.created))     
        
        self.render("mylinks.html",links=links,user=self.current_user)
    
class MeGroupHandler(BaseHandler):
    def get(self, groupid):
        group = self.db.get(LinkGroup, int(groupid))        
        self.render("megroup.html",group=group,user=self.current_user, links=group.links)

class StaffPicksHandler(BaseHandler):
    def get(self):
        follower_id = Select(FollowingUser.follower_id, FollowingUser.user_id==self.current_user.id)
        staffs = self.db.find(User,Not(User.id.is_in(follower_id)),User.id!=self.current_user.id)
        self.render("staff_picks.html",staffs=staffs,user=self.current_user)

class PopularGroupsHandler(BaseHandler):
    def get(self):
        group_id = Select(FollowingGroup.group_id, FollowingGroup.user_id==self.current_user.id)
        groups = self.db.find(LinkGroup, Not(LinkGroup.id.is_in(group_id)),User.id!=self.current_user.id)
        self.render("popular_groups.html",groups=groups,user=self.current_user)

class RecentLinksHandler(BaseHandler):
    def get(self):
        group_id = Select(LinkGroup.id, (LinkGroup.user_id==self.current_user.id))
        links = self.db.find(Link, Not(Link.group_id.is_in(group_id))).order_by(Desc(Link.created))
        self.render("recent_links.html",links=links,user=self.current_user)
        

class AddGroupHandler(BaseHandler):
    def get(self):
        self.render("addgroup.html", user = self.current_user,newgroup_msg="")

    def post(self):
        group_name = self.get_argument('groupname')
        group = self.db.find(LinkGroup,LinkGroup.user_id==self.current_user.id,LinkGroup.group_name==group_name).one()
        if not group:
            newgroup=LinkGroup()
            newgroup.user_id=self.current_user.id
            newgroup.group_name=group_name
            self.db.add(newgroup)
            self.db.commit()
            self.render("me.html",user=self.current_user)
        else:
            self.render("addgroup.html",user=self.current_user,newgroup_msg="your group_name has existed,please try again")

class DeleteGroupHandler(BaseHandler):
    def get(self,group_id):
        link_id =Select(Link.id, (Link.group_id==int(group_id)))
        links = self.db.find(Link, Link.id.is_in(link_id))
        for link in links:
            self.db.remove(link)
        group = self.db.find(LinkGroup,LinkGroup.id==int(group_id)).one()
        self.db.remove(group)
        self.db.commit()
        self.render("me.html",user=self.current_user)

class EditGroupHandler(BaseHandler):
    def get(self,group_id):
        group = self.db.find(LinkGroup,LinkGroup.id==int(group_id)).one()
        self.render("editgroup.html", user =self.current_user, group_name=group.group_name,group=group)
    def post(self,group_id):
        group_name = self.get_argument('groupname')
        group = self.db.find(LinkGroup,LinkGroup.id==int(group_id)).one()
        group.group_name = group_name
        self.db.commit()
        self.render("me.html",user=self.current_user)

class FollowingHandler(BaseHandler):
    def get(self):
        follower_id = Select(FollowingUser.follower_id,(FollowingUser.user_id==self.current_user.id))
        users = self.db.find(User, User.id.is_in(follower_id))
        group_id = Select(FollowingGroup.group_id,(FollowingGroup.user_id==self.current_user.id))
        groups = self.db.find(LinkGroup, LinkGroup.id.is_in(group_id))
        self.render("following.html",groups=groups,users=users,user=self.current_user)

class FollowerHandler(BaseHandler):
    def get(self):
        user_id = Select(FollowingUser.user_id,(FollowingUser.follower_id==self.current_user.id))        
        users = self.db.find(User, User.id.is_in(user_id))
        self.render("follower.html",users=users,user=self.current_user)
