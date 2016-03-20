from __future__ import unicode_literals

from django.db import models

from tfile.models import TFile

# Create your models here.

class Movie(models.Model):
    name_en = models.CharField(max_length = 1024, blank = True, verbose_name = 'English name')
    name_ru = models.CharField(max_length = 1024, blank = True, verbose_name = 'Russian name')
    year = models.IntegerField(blank = True, null = True, verbose_name = 'Year')
    kp_id = models.CharField(max_length = 2014, blank = True, verbose_name = 'Kinopoisk id')
    kp_parsed = models.BooleanField(default = False, verbose_name = 'Kinopoisk parsed')
    torrents = models.ManyToManyField(TFile, verbose_name = 'Torrents')
    
    def __unicode__(self):
        return self.name_en

