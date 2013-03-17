#encoding=utf-8
from  handlers.home import (HomeHandler,
                            HomeRecentHandler,
                            )

from  handlers.following import (FollowUserHandler,
                                 FollowGroupHandler,
                                 UnfollowUserHandler,
                                 UnfollowGroupHandler,
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
                         FollowerHandler,
                         MeHandler,
                         )

from handlers.group import GroupHandler

from handlers.link import (LinkSaveHandler,
                           CommentHandler,
                           AddCommentHandler,
                           EnterCommentHandler,
                           DeleteCommentHandler,
                           DeleteMylinkHandler,
                           LinkEditHandler,
                           LinkAddHandler,
                           LinkSaveEditHandler,
                           LinkMoveHandler,
                           )

from handlers.setting import (ProfileHandler,SettingsProfileHandler,SettingsAccountHandler,CancelAccountHandler)

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

        (r"/me/comment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",CommentHandler),
        (r"/me/addcomment/([0-9]+)",AddCommentHandler),
        (r"/me/entercomment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",EnterCommentHandler),
        (r"/me/deletecomment/([0-9]+)",DeleteCommentHandler),

        (r"/unfollow/user/([0-9]+)",UnfollowUserHandler),
        
        (r"/unfollow/group/([0-9]+)",UnfollowGroupHandler),

        (r"/user/([0-9]+)",UserHandler),
        (r"/redirect/pre", RedirectPageHandler),
        (r"/loadmore",LoadMoreHandler),

        (r"/delete/mylink/([0-9]+)",DeleteMylinkHandler),
        (r"/link/edit/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",LinkEditHandler),

        (r"/me/addlink",LinkAddHandler),
        (r"/test", TestHandler),
        (r"/upload", UploadHandler),
        (r"/link/save_edit/([0-9]+)", LinkSaveEditHandler),
        (r"/home_recent", HomeRecentHandler),
        (r"/me", MeHandler),
        (r"/link/move/(?P<group_id>[^\/]+)/?(?P<link_id>[^\/]+)?",LinkMoveHandler),
        (r"/setting/cancel_account",CancelAccountHandler),
        ]

 