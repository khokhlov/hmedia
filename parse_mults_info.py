#!/usr/bin/env python

from grab import Grab
import sys
from movie.kpparser import *
import time


url = sys.argv[1]

for url in sys.argv[1:]:
    try:
        m = MultsInfo(url)
    except:
        print url
        continue
    kpid = None
    name = None
    year = None
    try:
        kpid = KPMovie.get_by_name((u'%s' % m.name).encode('utf-8'))
    except:
        pass
    if kpid is not None:
        time.sleep(10)
        k = KPMovie(kpid)
        name = k.name_ru
        year = k.year
    print '%s %s (%s-%s %s-%s)' % (kpid, m.turl, m.name, m.year, name, year)
    time.sleep(10)
    