#coding:utf-8

from  handlers.home import HomeHandler

from  handlers.following import (FollowUserHandler,
                                 FollowGroupHandler,
                                 FollowerFollowUserHandler,
                                 FollowerUnfollowUserHandler,
                                 FollowingUnfollowUserHandler,
                                 FollowingUnfollowGroupHandler,
                                 GroupFollowGroupHandler,
                                 GroupUnfollowGroupHandler,
                                 UserFollowGroupHandler,
                                 UserUnfollowGroupHandler,
                                 UserFollowUserHandler,
                                 UserUnfollowUserHandler
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
                           DeleteCommentHandler
                           )

from handlers.setting import (ProfileHandler,SettingsProfileHandler,SettingsAccountHandler)

from handlers.setting import (ProfileHandler,SettingsProfileHandler)

from handlers.user import UserHandler

# test handler
from handlers.test import TestHandler

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
        (r"/me/settings/account",SettingsAccountHandler),
        (r"/group/logined/([0-9]+)", GroupLoginedHandler),

        (r"/me/comment/([0-9]+)",CommentHandler),
        (r"/me/addcomment/([0-9]+)",AddCommentHandler),
        (r"/me/deletecomment/([0-9]+)",DeleteCommentHandler),
        (r"/me/follower/follow/user/([0-9]+)",FollowUserHandler),
        (r"/me/follower/unfollow/user/([0-9]+)",FollowerUnfollowUserHandler),
        (r"/me/following/unfollow/user/([0-9]+)",FollowingUnfollowUserHandler),
        (r"/me/following/unfollow/group/([0-9]+)",FollowingUnfollowGroupHandler),

        (r"/user/([0-9]+)",UserHandler),
        (r"/user/follow/user/([0-9]+)",FollowUserHandler),
        (r"/user/unfollow/user/([0-9]+)",UserUnfollowUserHandler),
        (r"/group/follow/group/([0-9]+)",FollowGroupHandler),
        (r"/group/unfollow/group/([0-9]+)",GroupUnfollowGroupHandler),
        (r"/user/follow/group/([0-9]+)",FollowGroupHandler),
        (r"/user/unfollow/group/([0-9]+)",UserUnfollowGroupHandler),

        # (r"/hello/(?P<prepage>[^\/]+)", TestHandler),
        ]

 