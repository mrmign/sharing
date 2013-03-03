#!/usr/bin/env python
#coding=utf-8

import logging
import tornado.web

logger = logging.getLogger('share' + __name__)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


