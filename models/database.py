"""Mapping objects with database tables wiht storm ORM.

All the classes in this file are the objects used in 
the system. And add some foreign references to objects.
"""

# coding=utf-8

from storm.locals import *


class User(Storm):
    """The user object, the basic properties of user,
    and foreign references, such as user's own groups,
    the users and groups that he/she follows. 
    """
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
    """The group for links. we can get all the links that belongs to 
    the group, and can get the user the group belongs to.
    """
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
    """The link address object. It belongs to one group. There may be 
    duplicates. It is not unique.
    """
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
    likes = ReferenceSet("Link.id","LinkLike.link_id")


class FollowingUser(Storm):
    """One user follows others.
    """
    __storm_table__ = "following_user"
    id = Int(primary=True)
    user_id = Int()
    follower_id = Int()    


class FollowingGroup(Storm):
    """One user follows others' groups.
    """
    __storm_table__ = "following_group"
    id = Int(primary=True)
    user_id = Int()
    group_id = Int()


class Comment(Storm):
    """Comments to a link.
    """
    __storm_table__="comment"
    id =Int(primary=True)
    content =Unicode()
    user_id = Int()
    link_id = Int()
    created = DateTime()
    user = Reference(user_id, "User.id")

class LinkLike(Storm):
    """Records for one's like for links.
    """
    __storm_table__="linklike"
    id = Int(primary=True)
    user_id = Int()
    link_id = Int()


_database = create_database("mysql://root:root@localhost:3306/share")
store = Store(_database)
