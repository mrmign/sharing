# coding=utf-8

from storm.locals import *


class User(Storm):
    __storm_table__ = "user"
    id = Int(primary=True)
    username = Unicode()
    email = Unicode()
    password = Unicode()
    introduction = Unicode()
    follower_count = Int()

    groups = ReferenceSet("User.id", "LinkGroup.user_id")
    followings = ReferenceSet("User.id", "FollowingUser.user_id")
    following_groups = ReferenceSet("User.id", "FollowingGroup.user_id")


class LinkGroup(Storm):
    __storm_table__ = "linkgroup"
    id = Int(primary=True)
    user_id = Int()
    group_name = Unicode()
    private = Int()
    follower_count = Int()
    updated = DateTime()
    links_count = Int()
    description = Unicode()

    user = Reference(user_id, "User.id")
    links = ReferenceSet("LinkGroup.id", "Link.group_id")


class Link(Storm):
    __storm_table__ = "link"
    id = Int(primary=True)
    title = Unicode()
    url = Unicode()
    url_domain = Unicode()
    description = Unicode()
    comments_count = Int()
    like_count = Int()
    updated = DateTime()
    group_id = Int()

    linkgroup = Reference(group_id, "LinkGroup.id")
    comments = ReferenceSet("Link.id", "Comment.link_id")


class FollowingUser(Storm):
    __storm_table__ = "following_user"
    id = Int(primary=True)
    user_id = Int()
    follower_id = Int()    


class FollowingGroup(Storm):
    __storm_table__ = "following_group"
    id = Int(primary=True)
    user_id = Int()
    group_id = Int()


class Comment(Storm):
    __storm_table__ = "comment"
    id = Int(primary=True)
    content = Unicode()
    user_id = Int()
    link_id = Int()
    created = DateTime()
    user = Reference(user_id, "User.id")


_database = create_database("mysql://root:root@localhost:3306/share")
store = Store(_database)
