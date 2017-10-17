#!/usr/bin/env python
# encoding: utf-8

import codecs
import sys
import os
import csv
from datetime import date, timedelta
import datetime
import urllib
import time

import traceback
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hmedia.settings")
django.setup()

from django.conf import settings
 
from movie.models import Movie

delay = int(sys.argv[1])

q = Movie.objects.filter(kp_parsed=False)
        

for m in q:
    m.parse_kp()
    m.save()
    print m.name_ru
    time.sleep(delay)

