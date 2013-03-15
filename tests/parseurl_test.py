#! /usr/bin/env python
#encoding=utf-8

# from utils.processurl import ParseUrl

# url = "http://daringfireball.net/2010/07/improved_regex_for_matching_urls"

# parse = ParseUrl(url)
# print parse.domain, parse.title
import os
from bs4 import BeautifulSoup

from utils.cleanbookmark import cleanBookmarks
fi =  os.path.abspath(os.path.join(os.getcwd()) + "/uploads/22.html")
clean = cleanBookmarks(fi)
print clean
# soup = BeautifulSoup(open("bookmarks.html"))
# soup = BeautifulSoup(open("mac.html"))
# items = soup.find_all(["h3","a"])
# # print items
# print len(items)
