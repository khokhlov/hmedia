from django.contrib import admin

# Register your models here.

from .models import *

class TFileInlineAdmin(admin.StackedInline):
    model = Movie.torrents.through
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ru', 'year', 'kp_id', 'kp_parsed')
    exclude = ('torrents', )
    inlines = [TFileInlineAdmin, ]

admin.site.register(Movie, MovieAdmin)

