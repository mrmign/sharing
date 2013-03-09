#coding:utf-8

from  handlers.home import HomeHandler
# from  handlers.login import LoginHandler
# from  handlers.validate import ValidateHandler
# from  handlers.signup import SignupHandler
from handlers.auth import (LoginHandler,SignupHandler,LogoutHandler)
from handlers.group import (GroupHandler,MeGroupHandler)
url_patterns = [
        (r"/", HomeHandler),
        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        (r"/group/([0-9]+)", GroupHandler),
        (r"/me/group/([0-9]+)",MeGroupHandler),
        ]

 