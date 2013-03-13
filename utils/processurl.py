#encoding=utf-8
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup

class ParseUrl():
    def __init__(self, url):
        self._url = url
        self.domain = self.get_domain()
        self.title = self.get_title()

    def _request_url_content(self):
        url_encode = urllib2.urlopen(self._url)
        return url_encode.read()

    def get_title(self):
        html = self._request_url_content()
        soup = BeautifulSoup(html)
        return soup.title.string

    def get_domain(self):
         o = urlparse(self._url)
         return o.netloc