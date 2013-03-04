#coding:utf-8

import os

from uimodules import *

settings = dict(
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        ui_modules = {"HomeList": HomeListModule},
        debug=True,
        )
