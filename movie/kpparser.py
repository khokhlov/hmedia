#coding: utf-8

from grab import Grab
import pickle
from urllib2 import quote

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

KINOPOISK_URL = 'http://www.kinopoisk.ru/film/%s/'
KINOPOISK_SEARCH = 'https://www.kinopoisk.ru/index.php?first=yes&what=&kp_query=%s'

class KPMovie:
    def __init__(self, kid, cached = None):
        # Movie id.
        self.kid = kid
        self.g = Grab()
        self.cached = cached
                

        self.go()
    
    def go(self):
        if self.cached:
            print 'Loading from cache', self.kid
            c = ('%s' % self.cached).encode('cp1251', 'ignore')
            #print type(c)
            self.g.doc.body = c
            self.g.doc.parse()
        else:
            print 'Downloading', self.kid
            self.g.go(self._url())
            self.cached = self.g.doc.unicode_body()

        self.name_ru = self.g.doc('//h1[contains(@itemprop, "name")]').text()
        self.name_en = self.g.doc('//span[contains(@itemprop, "alternativeHeadline")]').text()
        self.year = self.g.doc('//table[contains(@class, "info")]/tr/*/div/a').text()
        self.genres = [el.text() for el in self.g.doc('//span[contains(@itemprop, "genre")]/a')]
        
    def _url(self):
        return KINOPOISK_URL % self.kid
    
    @staticmethod
    def get_by_name(name):
        url = KINOPOISK_SEARCH % quote(name)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        g = Grab(log_dir = 'tmp', referer = 'https://www.kinopoisk.ru/', headers = headers)
        g.go(url)
        return g.doc('//meta[@name="twitter:app:url:iphone"]/@content').text().split('/')[-1]

class MultsInfo:
    def __init__(self, url):
        self.url = url
        self.g = Grab()
        
        self.go()
    
    def go(self):
        self.g.go(self.url)
        self.name = self.g.doc('//html/body/center/div/div[2]/h1').text().split('"')[1]
        self.year = self.g.doc('//html/body/center/div/div[2]/div[3]/p[1]/a[1]').text().split()[1]
        self.turl = "http://mults.info/" + self.g.doc('//a[b="torrent"]/@href').text()

