# encoding=utf-8
from handlers.home import (HomeHandler,
                           HomeRecentHandler,
                           )

from handlers.follow import (FollowUserHandler,
                             FollowGroupHandler,
                             UnfollowUserHandler,
                             UnfollowGroupHandler,
                             )
from handlers.auth import (LoginHandler,
                           SignupHandler, 
                           LogoutHandler,
                           CancelHandler,
                           )

from handlers.me import (FeedHandler,
                         MyLinksHandler,
                         MeGroupHandler,
                         FollowingHandler,
                         FollowerHandler,
                         MeHandler,
                         )

from handlers.group import (GroupHandler,
                            AddGroupHandler,
                            DeleteGroupHandler,
                            EditGroupHandler,
                            )

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
                           LinkSearchHandler,
                           LinkLikeHandler,
                           CancelLinkLikeHandler,
                           )

from handlers.profile import (ProfileHandler, 
                              SettingsProfileHandler, 
                              SettingsAccountHandler,
                              )

from handlers.user import UserHandler

from handlers.recommend import (StaffPicksHandler,
                                PopularGroupsHandler,
                                RecentLinksHandler,
                                )

# test handler
from handlers.test import TestHandler

from handlers.redirect import RedirectPageHandler
from handlers.loadmore import LoadMoreHandler
from handlers.upload import UploadHandler
url_patterns = [
    (r"/", HomeHandler),

    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/signup", SignupHandler),

    (r"/group/([0-9]+)", GroupHandler),

    # (r"/link/save/?(?P<group_id>[0-9]+)?/?(?P<link_id>[0-9]+)?", LinkSaveHandler),
    (r"/link/save/(?P<group_id>[^\/]+)/?(?P<link_id>[^\/]+)?",
     LinkSaveHandler),

    (r"/me/feed", FeedHandler),
    (r"/me/mylinks", MyLinksHandler),
    (r"/me/following", FollowingHandler),
    (r"/me/follower", FollowerHandler),

    (r"/me/group/([0-9]+)", MeGroupHandler),

    (r"/me/addgroup", AddGroupHandler),
    (r"/me/deletegroup/([0-9]+)", DeleteGroupHandler),
    # (r"/me/editgroup/([0-9]+)",EditGroupHandler),
    (r"/me/editgroup/(?P<group_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",
     EditGroupHandler),


    (r"/follow/user/([0-9]+)", FollowUserHandler),
    (r"/follow/group/([0-9]+)", FollowGroupHandler),

    (r"/me/staff_picks", StaffPicksHandler),
    (r"/me/popular_groups", PopularGroupsHandler),
    (r"/me/recent_links", RecentLinksHandler),

    (r"/me/profile", ProfileHandler),
    (r"/me/settings/profile", SettingsProfileHandler),
    (r"/me/settings/account", SettingsAccountHandler),

    (r"/me/comment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",
     CommentHandler),
    (r"/me/addcomment/([0-9]+)", AddCommentHandler),
    (r"/me/entercomment/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",
     EnterCommentHandler),
    (r"/me/deletecomment/([0-9]+)", DeleteCommentHandler),

    (r"/unfollow/user/([0-9]+)", UnfollowUserHandler),

    (r"/unfollow/group/([0-9]+)", UnfollowGroupHandler),

    (r"/user/([0-9]+)", UserHandler),

    (r"/redirect/pre", RedirectPageHandler),
    (r"/loadmore", LoadMoreHandler),

    (r"/delete/mylink/([0-9]+)", DeleteMylinkHandler),
    (r"/link/edit/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?",
     LinkEditHandler),

    (r"/me/addlink", LinkAddHandler),
    (r"/test", TestHandler),
    (r"/upload", UploadHandler),
    (r"/link/save_edit/(?P<link_id>[^\/]+)/?(?P<previous_page>[^\/]+)?", LinkSaveEditHandler),
    (r"/home_recent", HomeRecentHandler),
    (r"/me", MeHandler),
    (r"/link/move/(?P<group_id>[^\/]+)/?(?P<link_id>[^\/]+)?",
     LinkMoveHandler),

    (r"/search/link", LinkSearchHandler),
    (r"/cancel", CancelHandler),

    (r"/like/([0-9]+)", LinkLikeHandler),
    (r"/cancel_like/([0-9]+)",CancelLinkLikeHandler),
]
