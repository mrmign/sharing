#coding=utf-8

from storm.locals import *

class User(Storm):
	__storm_table__ = "user"

	id = Int(primary=True)
	username = Unicode()
	email = Unicode()
	password = Unicode()
	introduction = Unicode()

	groups = ReferenceSet("User.id", "LinkGroup.user_id")
	followings = ReferenceSet("User.id", "Following.user_id")

class Following(Storm):
	__storm_table__="following"
	id = Int(primary=True)
	user_id = Int()
	follower_id =Int()

	# groups = ReferenceSet("Following.follower_id", "LinkGroup.user_id")

class LinkGroup(Storm):
	__storm_table__ = "linkgroup"

	id = Int(primary=True)
	user_id = Int()
	group_name = Unicode()
	follower_count = Int()
	like_count = Int()
	updated = DateTime()
	created = DateTime()
	links_count = Int()

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
	created = DateTime()
	updated = DateTime()
	group_id = Int()

	linkgroup = Reference(group_id, "LinkGroup.id")



_database = create_database("mysql://root:root@localhost:3306/share")
store = Store(_database)
