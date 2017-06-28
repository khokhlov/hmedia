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
    list_display = ('name_ru', 'name_en', 'year', 'watched_flag', 'kp_id', 'kp_parsed')
    list_editable = ('watched_flag',)
    exclude = ('torrents', 'movie_dir')
    inlines = [TFileInlineAdmin, MovieDirInlineAdmin]
    actions = [parse_kp, ]
    list_filter = ('watched_flag', 'genres')
    search_fields = ['name_ru', 'name_en', 'year']

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDir)
admin.site.register(Genre)

