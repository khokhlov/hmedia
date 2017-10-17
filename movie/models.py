#coding: utf-8

from __future__ import unicode_literals

import re

from django.db import models
from django.conf import settings

from tfile.models import TFile

from .kpparser import KPMovie

import sys
import os

reload(sys)  
sys.setdefaultencoding('utf8')
# Create your models here.

class MovieDir(models.Model):
    name = models.CharField(max_length = 1024, verbose_name = 'Dir')
    
    def __unicode__(self):
        return self.name
    
    @staticmethod
    def has(name):
        return MovieDir.objects.filter(name = name).count() > 0
    
    @staticmethod
    def get(name):
        return MovieDir.objects.filter(name = name)[0]
    
    @staticmethod
    def get_or_create(name):
        if MovieDir.has(name):
            return MovieDir.get(name)
        g = MovieDir()
        g.name = name
        g.save()
        return g
    
    def get_path(self):
        return os.path.join(settings.LINKS_PATH_TAGS, self.name)


class Genre(models.Model):
    name = models.CharField(max_length = 1024, verbose_name = 'Genre')
    
    def __unicode__(self):
        return self.name
    
    @staticmethod
    def has(genre):
        return Genre.objects.filter(name = genre).count() > 0
    
    @staticmethod
    def get(genre):
        return Genre.objects.filter(name = genre)[0]
    
    @staticmethod
    def get_or_create(genre):
        if Genre.has(genre):
            return Genre.get(genre)
        g = Genre()
        g.name = genre
        g.save()
        return g
    
    def get_path(self):
        return os.path.join(settings.LINKS_PATH_GENRE, self.name)

class Movie(models.Model):
    name_en = models.CharField(max_length = 1024, blank = True, verbose_name = 'English name')
    name_ru = models.CharField(max_length = 1024, blank = True, verbose_name = 'Russian name')
    year = models.IntegerField(blank = True, null = True, verbose_name = 'Year')
    kp_id = models.CharField(max_length = 2014, blank = True, verbose_name = 'Kinopoisk id')
    kp_parsed = models.BooleanField(default = False, verbose_name = 'Kinopoisk parsed')
    torrents = models.ManyToManyField(TFile, verbose_name = 'Torrents')
    movie_dir = models.ManyToManyField(MovieDir, verbose_name = 'Dirs')
    cached = models.TextField(blank = True, null = True, verbose_name = 'Kinopoisk cache')
    genres = models.ManyToManyField(Genre, blank = True, verbose_name = 'Genres')
    watched_flag = models.BooleanField(default = False, verbose_name = 'Watched')
    
    def __unicode__(self):
        return self.name_en
    
    def path(self):
        return u'%s(%s)[%s]' % (self.name_ru, self.name_en, self.year)
    
    def parse_kp(self):
        m = KPMovie(self.get_kp_id(), self.cached)
        self.name_en = u'%s' % m.name_en
        self.name_ru = u'%s' % m.name_ru
        self.year = int(m.year)
        
        self.genres.clear()
        for g in m.genres:
            self.genres.add(Genre.get_or_create(g))

        self.kp_parsed = True
        self.cached = m.cached
        self.save()
    
    def get_kp_id(self):
        m = re.search('http[s]*://www.kinopoisk.ru/film/(\d+)', self.kp_id)
        if m:
            return m.group(1)
        return self.kp_id
    
    def get_paths(self):
        paths = []
        for g in self.genres.all():
            if self.watched_flag:
                paths.append(os.path.join(settings.LINKS_PATH_WATCHED, g.get_path(), self.path()))
            else:
                paths.append(os.path.join(settings.LINKS_PATH_UNWATCHED, g.get_path(), self.path()))
            paths.append(os.path.join(settings.LINKS_PATH_ALL, g.get_path(), self.path()))
        for g in self.movie_dir.all():
            paths.append(os.path.join(settings.LINKS_PATH_ALL, g.get_path(), self.path()))
        return paths
    
    @staticmethod
    def get(kpid):
        q = Movie.objects.filter(kp_id__contains=kpid)
        for m in q.all():
            if m.get_kp_id() == kpid:
                return m
        return None



