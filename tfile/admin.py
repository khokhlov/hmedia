from django.contrib import admin

# Register your models here.

from .models import *


def resave(modeladmin, request, queryset):
    for o in queryset.all():
        o.clean()
        o.save()

def copy_to_client(modeladmin, request, queryset):
    for o in queryset.all():
        o.copy_to_client()
        
class TFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tfile', 'url', 'downloaded')
    
    actions = [resave, copy_to_client]
    
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('files',)

admin.site.register(TFile, TFileAdmin)

