#coding:utf-8

from  handlers.home import HomeHandler

from  handlers.following import (FollowUserHandler,FollowGroupHandler)
from handlers.auth import (LoginHandler,SignupHandler,LogoutHandler)
from handlers.me import (FeedHandler,
                         MyLinksHandler,
                         MeGroupHandler,
                         StaffPicksHandler,
                         PopularGroupsHandler,
                         RecentLinksHandler,

                         FollowingHandler,
                         FollowerHandler


                         )

from handlers.group import GroupHandler

from handlers.link import LinkSaveHandler

url_patterns = [

        (r"/group/([0-9]+)", GroupHandler),
        (r"/", HomeHandler),

        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        
        (r"/group/([0-9]+)", GroupHandler),

        (r"/link/save/([0-9]+)", LinkSaveHandler),


        (r"/me/feed", FeedHandler),
        (r"/me/mylinks", MyLinksHandler),
        (r"/me/following", FollowingHandler),
        (r"/me/follower", FollowerHandler),
        
        (r"/me/group/([0-9]+)",MeGroupHandler),

        (r"/follow/user/([0-9]+)",FollowUserHandler),
        (r"/follow/group/([0-9]+)",FollowGroupHandler),       
        (r"/me/staff_picks",StaffPicksHandler),
        (r"/me/popular_groups",PopularGroupsHandler),
        (r"/me/recent_links",RecentLinksHandler),

        ]

 