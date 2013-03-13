#coding=utf-8

from utils.processurl import ParseUrl

url = "http://daringfireball.net/2010/07/improved_regex_for_matching_urls"

parse = ParseUrl(url)
print parse.domain, parse.title