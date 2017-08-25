#!/usr/bin/env python
# encoding: utf-8

import codecs
import sys
import os
import csv
from datetime import date, timedelta
import datetime
import urllib

import traceback
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hmedia.settings")
django.setup()

from django.conf import settings
 
from movie.models import Movie, MovieDir
from tfile.models import TFile
from django.core.files import File

tag = sys.argv[1]

md = MovieDir.get_or_create(tag)

for l in open(sys.argv[2]):
    v = l.strip().split()
    if len(v) > 1 and v[1][0] == 'h':
        kpid = v[0]
        turl = v[1]
        print 'Adding', kpid, turl
        m = Movie.get(kpid)
        if m is None:
            m = Movie()
            m.kp_id = kpid
            m.save()
        m.movie_dir.add(md)
        m.save()
        
        t = TFile()
        t.url = turl
        result = urllib.urlretrieve(turl)
        t.tfile.save(
                os.path.basename(turl),
                File(open(result[0]))
                )
        t.save()
        
        m.torrents.add(t)
        m.save()
        


