from django.contrib import admin

from . import models
from someapp.models import Album, Track

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'artist']
    
    
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['album', 'order', 'title', 'duration']


