#encoding=utf-8
from  handlers.home import HomeHandler

from  handlers.following import (FollowUserHandler,
                                 FollowGroupHandler,
                                 UnfollowUserHandler,
                                 UnfollowGroupHandler
                                 )
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

from handlers.group import (GroupHandler,
                           GroupLoginedHandler                           
                           )

from handlers.link import (LinkSaveHandler,
                           CommentHandler,
                           AddCommentHandler,
                           EnterCommentHandler,
                           DeleteCommentHandler,
                           DeleteMylinkHandler,
                           LinkEditHandler,
                           LinkAddHandler,
                           )

from handlers.setting import (ProfileHandler,SettingsProfileHandler,SettingsAccountHandler)

from handlers.setting import (ProfileHandler,SettingsProfileHandler)

from handlers.user import UserHandler

# test handler
from handlers.test import TestHandler

from handlers.redirect import RedirectPageHandler
from handlers.loadmore import LoadMoreHandler
from handlers.upload import UploadHandler
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
        # (r"/me/editgroup/([0-9]+)",EditGroupHandler),
        (r"/me/editgroup/(?P<group_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",EditGroupHandler),


        (r"/follow/user/([0-9]+)",FollowUserHandler),
        (r"/follow/group/([0-9]+)",FollowGroupHandler),      

        (r"/me/staff_picks",StaffPicksHandler),
        (r"/me/popular_groups",PopularGroupsHandler),
        (r"/me/recent_links",RecentLinksHandler),

        (r"/me/profile",ProfileHandler),
        (r"/me/settings/profile",SettingsProfileHandler),
        (r"/me/settings/account",SettingsAccountHandler),
        (r"/group/logined/([0-9]+)", GroupLoginedHandler),

        (r"/me/comment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",CommentHandler),
        (r"/me/addcomment/([0-9]+)",AddCommentHandler),
        (r"/me/entercomment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",EnterCommentHandler),
        (r"/me/deletecomment/([0-9]+)",DeleteCommentHandler),

        (r"/unfollow/user/([0-9]+)",UnfollowUserHandler),
        
        (r"/unfollow/group/([0-9]+)",UnfollowGroupHandler),

        (r"/user/([0-9]+)",UserHandler),
      

        (r"/redirect/pre", RedirectPageHandler),
        (r"/delete/mylink/([0-9]+)",DeleteMylinkHandler),
        (r"/link/edit/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",LinkEditHandler),

        (r"/me/addlink",LinkAddHandler),
       
        (r"/loadmore",LoadMoreHandler),

        (r"/test", TestHandler),
        (r"/upload", UploadHandler),
        ]

 