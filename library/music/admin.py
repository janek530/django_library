from django.contrib import admin
from .models import Album, Song

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)