from django.contrib import admin

# Register your models here.

from .models import *

class TFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tfile', 'url', 'downloaded')

admin.site.register(TFile, TFileAdmin)

