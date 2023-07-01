
from django.urls import path, include
from .views import index, about, song, add_album, edit_song
from .serializer import AlbumSerializer
from rest_framework import viewsets, routers
from .models import Album
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

route = routers.DefaultRouter()
route.register(r'album', AlbumViewSet)

urlpatterns = [
    path('', index),
    path('add/', add_album),
    path('<str:name>/', about),
    path('<str:name>/<int:number>/', song, name='song_details'),
    path('<str:name>/<int:number>/edit_song', edit_song, name='edit_song'),
    path('api-album/', include(route.urls))
]