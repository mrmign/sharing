#coding=utf-8

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):        
        self.render("login.html",login_msg=" ")
