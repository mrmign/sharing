"""Classes related to link.

1. Save a link from others'.
2. Comment to a link.
3. Add a new link.
4. Like a link.
"""

# encoding=utf-8

import tornado.web
from tornado.escape import url_escape

from base import BaseHandler
from models.database import Link, LinkGroup, Comment,LinkLike
from utils.processurl import ParseUrl
from storm.expr import (Desc, Asc, Select, Like)


class LinkSaveHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, group_id, link_id):
        g = self.db.get(LinkGroup, int(group_id))
        g.links_count += 1
        l = self.db.get(Link, int(link_id))
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
    def get(self, link_id, previous_page):
        # print previous_page
        # print url_escape(previous_page)
        self.set_secure_cookie("previous", url_escape(previous_page))
        l = self.db.get(Link, int(link_id))
        self.render("comment.html", user=self.current_user, link=l)


class AddCommentHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, link_id):
        l = self.db.get(Link, int(link_id))
        cmt = self.get_argument('add_comment')
        comment = Comment()
        comment.content = cmt
        comment.user_id = self.current_user.id
        comment.link_id = int(link_id)
        l.comments_count += 1
        self.db.add(comment)

        self.db.commit()
        self.render("comment.html", user=self.current_user, link=l)


class EnterCommentHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, link_id, previous_page):
        l = self.db.get(Link, int(link_id))
        cmt = self.get_argument('enter')
        comment = Comment()
        comment.content = cmt
        comment.user_id = self.current_user.id
        comment.link_id = int(link_id)
        l.comments_count += 1
        self.db.add(comment)

        self.db.commit()
        self.redirect(previous_page)


class DeleteCommentHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, comment_id):
        comment = self.db.get(Comment, int(comment_id))
        l = self.db.get(Link, int(comment.link_id))
        self.db.remove(comment)
        l.comments_count -= 1
        self.db.commit()
        self.render("comment.html", user=self.current_user, link=l)


class DeleteMylinkHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, link_id):
        link = self.db.get(Link, int(link_id))
        for comment in link.comments:
            self.db.remove(comment)
        for like in link.likes:
            self.db.remove(like)
        group = self.db.get(LinkGroup, link.linkgroup.id)
        group.links_count -= 1
        self.db.remove(link)
        self.db.commit()
        self.redirect(self.previous)


class LinkEditHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, link_id, previous_page):
        self.set_secure_cookie("previous", url_escape(previous_page))
        link = self.db.get(Link, int(link_id))
        self.render("link_edit.html", user=self.current_user, link=link)


class LinkAddHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        url = self.get_argument('url')
        group_id = self.get_argument('hd')
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


class LinkSaveEditHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, link_id, previous_page):
        l = self.db.get(Link, int(link_id))
        l.title = self.get_argument('link_title')
        l.description = self.get_argument('link_description',u'')
        self.db.commit()
        self.redirect(previous_page)


class LinkMoveHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, group_id, link_id):
        l = self.db.get(Link, int(link_id))
        l.linkgroup.links_count -= 1
        l.group_id = int(group_id)
        group = self.db.get(LinkGroup, int(group_id))
        group.links_count += 1
        self.db.commit()
        self.redirect(self.previous)


class LinkSearchHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        text = self.get_argument('q')
        sub = Select(LinkGroup.id, (LinkGroup.user_id == self.current_user.id))
        link_id = Select(Link.id, (Link.group_id.is_in(sub)))
        links = self.db.find(Link, Link.id.is_in(link_id), Link.title.like(
            "%"+text+"%")).order_by(Desc(Link.updated))
        self.render(
            "search.html", user=self.current_user, links=links, text=text)

class LinkLikeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,link_id):
        l = self.db.get(Link, int(link_id))
        l.like_count += 1
        like = LinkLike()
        like.user_id = self.current_user.id
        like.link_id = int(link_id)
        self.db.add(like)
        self.db.commit()
        self.redirect(self.previous)

class CancelLinkLikeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,link_id):
        l = self.db.get(Link, int(link_id))
        l.like_count -=1
        like = self.db.find(LinkLike, LinkLike.user_id == self.current_user.id,
            LinkLike.link_id == int(link_id)).one()
        self.db.remove(like)
        self.db.commit()
        self.redirect(self.previous)


