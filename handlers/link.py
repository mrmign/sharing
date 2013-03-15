#encoding=utf-8

import tornado.web
from tornado.escape import url_escape

from base import BaseHandler
from models.database import Link,LinkGroup,Comment
from utils.processurl import ParseUrl

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
        self.redirect(self.previous)


class CommentHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self,link_id, previous_page):
        # print previous_page
        # print url_escape(previous_page)
        self.set_secure_cookie("previous",url_escape(previous_page))
        l = self.db.get(Link,int(link_id))
        self.render("comment.html" ,user=self.current_user,link=l)
        

class AddCommentHandler(BaseHandler):
    def get(self,link_id):
        l = self.db.get(Link,int(link_id))
        cmt = self.get_argument('add_comment')
        comment =Comment()
        comment.content = cmt
        comment.user_id = self.current_user.id
        comment.link_id = int(link_id)
        l.comments_count += 1
        self.db.add(comment)

        self.db.commit()
        self.render("comment.html" ,user=self.current_user,link=l)

class EnterCommentHandler(BaseHandler):
    def get(self,link_id,previous_page):
        l = self.db.get(Link,int(link_id))
        cmt = self.get_argument('enter')
        comment =Comment()
        comment.content = cmt
        comment.user_id = self.current_user.id
        comment.link_id = int(link_id)
        l.comments_count += 1
        self.db.add(comment)

        self.db.commit()
        self.redirect(previous_page)

class DeleteCommentHandler(BaseHandler):
    def get(self,comment_id):
        comment = self.db.get(Comment,int(comment_id))
        l = self.db.get(Link,int(comment.link_id))
        link_owner = l.linkgroup.user
        if comment.user_id==self.current_user.id or link_owner.id==self.current_user.id:
            self.db.remove(comment)
            l.comments_count -= 1
            self.db.commit()
        self.render("comment.html" ,user=self.current_user,link=l)

class DeleteMylinkHandler(BaseHandler):
    def get(self,link_id):
        link = self.db.get(Link,int(link_id))
        self.db.remove(link)
        self.db.commit()
        self.redirect(self.previous)

class LinkEditHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self,link_id, previous_page):
        # print previous_page
        # print url_escape(previous_page)
        self.set_secure_cookie("previous",url_escape(previous_page))
        link = self.db.get(Link,int(link_id))
        self.render("link_edit.html" ,user=self.current_user,link=link)
class LinkAddHandler(BaseHandler):
    def get(self):
        url = self.get_argument('url')
        group_id =self.get_argument('hd')
        # print url
        # print group_id
        parse = ParseUrl(url)
        link = Link()
        link.title = parse.title
        link.url = url
        link.url_domain = parse.domain
        link.group_id = int(group_id)
        self.db.add(link)
        group = self.db.get(LinkGroup, int(group_id))
        group.links_count += 1
        self.db.commit()
        self.redirect("/me/group/{0}".format(group_id))
        # self.render("megroup.html",group=group,user=self.current_user, links=group.links)
        
