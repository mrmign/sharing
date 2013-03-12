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
                         AddGroupHandler,
                         DeleteGroupHandler,
                         EditGroupHandler,
                         FollowingHandler,
                         FollowerHandler
                         )

from handlers.group import (GroupHandler,GroupLoginedHandler)

from handlers.link import LinkSaveHandler

from handlers.setting import (ProfileHandler,SettingsProfileHandler)
url_patterns = [
        (r"/", HomeHandler),

        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler),
        (r"/signup",SignupHandler),
        
        (r"/group/([0-9]+)", GroupHandler),

        # (r"/link/save/?(?P<group_id>[0-9]+)?/?(?P<link_id>[0-9]+)?", LinkSaveHandler),
        (r"/link/save/(?P<group_id>[^\/]+)/?(?P<link_id>[^\/]+)?", LinkSaveHandler),

        (r"/me/feed", FeedHandler),
        (r"/me/mylinks", MyLinksHandler),
        (r"/me/following", FollowingHandler),
        (r"/me/follower", FollowerHandler),
        
        (r"/me/group/([0-9]+)",MeGroupHandler),
        
        (r"/me/addgroup",AddGroupHandler),
        (r"/me/deletegroup/([0-9]+)",DeleteGroupHandler),
        (r"/me/editgroup/([0-9]+)",EditGroupHandler),

        (r"/follow/user/([0-9]+)",FollowUserHandler),
        (r"/follow/group/([0-9]+)",FollowGroupHandler),      

        (r"/me/staff_picks",StaffPicksHandler),
        (r"/me/popular_groups",PopularGroupsHandler),
        (r"/me/recent_links",RecentLinksHandler),

        (r"/me/profile",ProfileHandler),
        (r"/me/settings/profile",SettingsProfileHandler),
        (r"/group/logined/([0-9]+)", GroupLoginedHandler),
      
        ]

 