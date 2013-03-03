#!/usr/bin/env python
#coding:utf-8

from  handlers.home import HomeHandler

url_patterns = [
        (r"/", HomeHandler),
        ]

