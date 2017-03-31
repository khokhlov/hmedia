#coding: utf-8

from grab import Grab
import pickle

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

KINOPOISK_URL = 'http://www.kinopoisk.ru/film/%s/'

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

