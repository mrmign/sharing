from models.database import (User, LinkGroup, Link, store)
from storm.expr import (Desc,Asc, Select)

sub = Select(LinkGroup.id, (LinkGroup.user_id==7))
result = store.find(Link, Link.group_id.is_in(sub)).order_by(Desc(Link.created))
for l in result:
    print l.title, l.created

# user = store.get(User,1)
# print user.username
# print user.groups.count()

# for g in user.groups:
# 	for l in g.links:
# 		print l.title


# lg = store.get(LinkGroup, 1)
# print lg.group_name, lg.user.username
# print lg.links.count()

# print type(lg.links.order_by()[:7])

# link = store.get(Link, 1)
# print link.title, link.url_domain, link.linkgroup.group_name, link.linkgroup.user.username

# link = store.find(Link, Link.group_id==1)
# for l in link.order_by(Desc(Link.created))[:7]:
# 	print l.title, l.created

# groups = store.find(LinkGroup)
# # print groups.count()
# for group in groups:
# 	print group.user.id
# # group = store.get(LinkGroup, 2)
# groups = store.find(LinkGroup)
# for g in groups:
# 	for li in g.links:
# 		print li.title
# 	print "***************************"