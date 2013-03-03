#!/usr/bin/env python
#coding:utf-8

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

from urls import url_patterns as handlers
from settings import settings
from models.database import store as db

define("port", default=8000, help="server port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
    	self.db = db
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
        
if __name__ == "__main__":
    main()





