from django.contrib import admin

# Register your models here.

from .models import *

class TFileInlineAdmin(admin.StackedInline):
    model = Movie.torrents.through
    extra = 1

class MovieDirInlineAdmin(admin.StackedInline):
    model = Movie.movie_dir.through
    extra = 1

def parse_kp(modeladmin, request, queryset):
    for o in queryset.all():
        o.parse_kp()

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'year', 'kp_id', 'kp_parsed')
    exclude = ('torrents', 'movie_dir')
    inlines = [TFileInlineAdmin, MovieDirInlineAdmin]
    actions = [parse_kp, ]

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDir)
admin.site.register(Genre)

