# coding:utf-8

import os

from uimodules import *

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    ui_modules={"HomeList": HomeListModule},
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url="/login",
    debug=True,
)

NUM_FEED = 10
NUM_RECENT_LINKS = 15