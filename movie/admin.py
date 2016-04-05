from django.contrib import admin

# Register your models here.

from .models import *

class TFileInlineAdmin(admin.StackedInline):
    model = Movie.torrents.through
    extra = 1

def parse_kp(modeladmin, request, queryset):
    for o in queryset.all():
        o.parse_kp()

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ru', 'year', 'kp_id', 'kp_parsed')
    exclude = ('torrents', )
    inlines = [TFileInlineAdmin, ]
    actions = [parse_kp, ]

admin.site.register(Movie, MovieAdmin)

