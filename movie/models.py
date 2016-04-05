#coding: utf-8

from __future__ import unicode_literals

import re

from django.db import models

from tfile.models import TFile

from .kpparser import KPMovie

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
# Create your models here.

class Movie(models.Model):
    name_en = models.CharField(max_length = 1024, blank = True, verbose_name = 'English name')
    name_ru = models.CharField(max_length = 1024, blank = True, verbose_name = 'Russian name')
    year = models.IntegerField(blank = True, null = True, verbose_name = 'Year')
    kp_id = models.CharField(max_length = 2014, blank = True, verbose_name = 'Kinopoisk id')
    kp_parsed = models.BooleanField(default = False, verbose_name = 'Kinopoisk parsed')
    torrents = models.ManyToManyField(TFile, verbose_name = 'Torrents')
    
    cached = models.TextField(blank = True, null = True, verbose_name = 'Kinopoisk cache')
    
    def __unicode__(self):
        return self.name_en
    
    def parse_kp(self):
        m = KPMovie(self.get_kp_id(), self.cached)
        self.name_en = u'%s' % m.name_en
        self.name_ru = u'%s' % m.name_ru
        self.year = int(m.year)
        self.kp_parsed = True
        self.cached = m.cached
        self.save()
    
    def get_kp_id(self):
        m = re.search('http://www.kinopoisk.ru/film/(\d+)', self.kp_id)
        if m:
            return m.group(1)
        return self.kp_id
           
