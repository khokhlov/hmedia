#!/usr/bin/env python
# encoding: utf-8

import codecs
import sys
import os
import csv
from datetime import date, timedelta
import datetime

import traceback
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hmedia.settings")
django.setup()

from django.conf import settings

def create_path(p):
    try:
        os.makedirs(p)
    except:
        pass

def create_link(f, t):
    try:
        os.symlink(f, t)
    except Exception as e:
        print 'Error %s -> %s: %s' % (f, t, str(e))


# genres
from movie.models import Genre
for g in Genre.objects.all():
    gpath = settings.LINKS_PATH_GENRE % g.name
    create_path(gpath)
    for f in g.movie_set.all():
        mpath = '%s/%s' % (gpath, f.path())
        create_path(mpath)
        print f.path()
        for t in f.torrents.all():
            link_from = t.get_torrent_download_path()
            link_to = '%s/%s' % (mpath, t.name)
            create_link(link_from, link_to)
            
