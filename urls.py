#coding:utf-8

from  handlers.home import HomeHandler

from handlers.auth import (LoginHandler,SignupHandler,LogoutHandler)
from handlers.me import (FeedHandler,
                         MyLinksHandler,
                         MeGroupHandler,
                         StaffPicksHandler,
                         PopularGroupsHandler,
                         RecentLinksHandler,
                         NewGroupHandler,
                         )

from handlers.group import GroupHandler

url_patterns = [
        (r"/", HomeHandler),
        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        (r"/group/([0-9]+)", GroupHandler),
        (r"/feed", FeedHandler),
        (r"/mylinks", MyLinksHandler),
        (r"/me/group/([0-9]+)",MeGroupHandler),
        (r"/staff_picks",StaffPicksHandler),
        (r"/popular_groups",PopularGroupsHandler),
        (r"/recent_links",RecentLinksHandler),
        (r"/me/newgroup",NewGroupHandler),
        ]

 