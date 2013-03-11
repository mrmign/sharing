#coding:utf-8

from  handlers.home import HomeHandler

from  handlers.following import FollowHandler
from handlers.auth import (LoginHandler,SignupHandler,LogoutHandler)
from handlers.me import (FeedHandler,
                         MyLinksHandler,
                         MeGroupHandler,
                         StaffPicksHandler,
                         PopularGroupsHandler,
                         RecentLinksHandler,
                         AddGroupHandler,
                         DeleteGroupHandler,
                         EditGroupHandler,
                         )

from handlers.group import GroupHandler

from handlers.link import LinkSaveHandler

url_patterns = [
        (r"/", HomeHandler),
        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        (r"/group/([0-9]+)", GroupHandler),

        (r"/link/save/([0-9]+)", LinkSaveHandler),

        (r"/me/feed", FeedHandler),
        (r"/me/mylinks", MyLinksHandler),
        (r"/me/group/([0-9]+)",MeGroupHandler),
        (r"/me/addgroup",AddGroupHandler),
        (r"/me/deletegroup/([0-9]+)",DeleteGroupHandler),
        (r"/me/editgroup/([0-9]+)",EditGroupHandler),
        (r"/me/staff_picks",StaffPicksHandler),
        (r"/me/popular_groups",PopularGroupsHandler),
        (r"/me/recent_links",RecentLinksHandler),
        (r"/follow/user/([0-9]+)",FollowHandler),
        ]

 