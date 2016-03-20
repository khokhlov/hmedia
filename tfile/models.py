from __future__ import unicode_literals

import md5
import datetime

from django.db import models

# Create your models here.

def tfile_upload(instance, filename):
    d = md5.md5('%s %s' % (datetime.datetime.now(), filename)).hexdigest()
    return 'torrents/%s_%s' % (d, filename)

class TFile(models.Model):
    name = models.CharField(max_length = 256, blank = True, null = True, verbose_name = 'Torrent name')
    url = models.URLField(max_length = 1024, blank = True, null = True, verbose_name = 'Torrent URL')
    downloaded = models.BooleanField(default = False, verbose_name = 'Is downloaded')
    tfile = models.FileField(upload_to = tfile_upload, blank = True, verbose_name = 'Torrent file')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
