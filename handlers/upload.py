"""Upload class to deal with the bookmark file 
uploaded by user, remove useless tag and add 
links in the file to database link table.
"""

# encoding=utf-8
import os
import uuid
from urlparse import urlparse
from base import BaseHandler
from bs4 import BeautifulSoup
from models.database import LinkGroup, Link
from utils.cleanbookmark import cleanBookmarks
__UPLOADS__ = "uploads/"


class UploadHandler(BaseHandler):
    def get(self):
        self.render("upload.html", user=self.current_user)

    def post(self):
        fileinfo = self.request.files['import_file'][0]
        # print "fileinfo is", fileinfo
        # fname = fileinfo['filename']
        # extn = os.path.splitext(fname)[1]
        # bookmark name
        # self.bk = str(self.current_user.id) + extn
        # fh = open(__UPLOADS__ + self.bk, 'w')
        # fh.write(fileinfo['body'])

        # save imported bookmarks to db
        self._parse_bookmark_file(fileinfo['body'])

        self.redirect("/me/mylinks")

    def _parse_bookmark_file(self, body):
        """Retidy the file first, then add each link item
        to the database.
        """
        imp = LinkGroup()
        imp.user_id = self.current_user.id
        imp.group_name = u"Imported Bookmarks"
        imp.private = 1

        cleaned = cleanBookmarks(body)
        soup = BeautifulSoup(cleaned)
        items = soup.find_all("a")
        imp.links_count = len(items)
        self.db.add(imp)
        self.db.commit()
        # fi = os.path.abspath(os.path.join(os.getcwd()) + "/uploads/" +
        # str(self.current_user.id) + ".html")

        for item in items:
            link = Link()
            link.group_id = imp.id
            link.title = unicode(item.get_text())
            link.url = unicode(item.get("href"))
            link.url_domain = unicode(self.get_domain(link.url))
            self.db.add(link)
            imp.link_count = imp.links_count + 1
            self.db.commit()

    def get_domain(self, url):
        """Get the link url's domain"""
        o = urlparse(url)
        return o.netloc
