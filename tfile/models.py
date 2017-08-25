# coding: utf-8

from __future__ import unicode_literals

import md5
import datetime
import shutil

from django.db import models
from django.conf import settings

from .decode import *

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Create your models here.

def tfile_upload(instance, filename):
    d = md5.md5('%s %s' % (datetime.datetime.now(), filename)).hexdigest()
    return 'torrents/%s_%s' % (d, filename)

class TFile(models.Model):
    name = models.CharField(max_length = 256, blank = True, null = True, verbose_name = 'Torrent name')
    url = models.URLField(max_length = 1024, blank = True, null = True, verbose_name = 'Torrent URL')
    downloaded = models.BooleanField(default = False, verbose_name = 'Is downloaded')
    tfile = models.FileField(upload_to = tfile_upload, blank = True, verbose_name = 'Torrent file')
    comment = models.TextField(null = True, blank = True, verbose_name = 'Comment')
    files = models.TextField(null = True, blank = True, verbose_name = 'Files')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    def get_torrent_download_path(self):
        if self.name is None or self.name == '':
            self.clean()
            self.save()
        return "%s/%s"% (settings.TORRENT_DOWNLOAD_PATH, self.name)
    
    def get_torrent_file_path(self):
        return "%s/%s"% (settings.TORRENT_STORAGE_ROOT, self.tfile)
    
    def get_client_file_path(self):
        return "%s/%s.torrent"% (settings.TORRENT_CLIENT_PATH, self.pk)
    
    def copy_to_client(self):
        shutil.copy(self.get_torrent_file_path(), self.get_client_file_path())
    
    def get_torrent_name(self):
        return torrent_name(open(self.get_torrent_file_path(), mode='rb').read())
    
    def clean(self):
        p = u'Can\'t parse torrent'
        try:
            p = self.get_torrent_name()
            print p
#            if self.name is None or self.name == '':
#                self.name = p
        except:
            pass
	if self.name is None or self.name == '':
		self.name = p
        self.files = u'Name: %s\n' % p.decode('utf-8')

