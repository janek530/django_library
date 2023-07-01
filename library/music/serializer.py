from .models import Album, Song
from rest_framework import serializers

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'type', 'songs', 'year_of_publish', 'image', 'is_borrowed']
