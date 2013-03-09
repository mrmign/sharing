#coding:utf-8

from  handlers.home import HomeHandler
# from  handlers.login import LoginHandler
# from  handlers.validate import ValidateHandler
# from  handlers.signup import SignupHandler
from handlers.auth import (LoginHandler,SignupHandler,LogoutHandler)
from handlers.me import (FeedHandler,MyLinksHandler)
from handlers.group import GroupHandler
url_patterns = [
        (r"/", HomeHandler),
        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        (r"/group/([0-9]+)", GroupHandler),
        (r"/feed", FeedHandler),
        (r"/mylinks", MyLinksHandler),
        ]

 