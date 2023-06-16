
from django.urls import path
from .views import index, about, song, add_album

urlpatterns = [
    path('', index),
    path('add/', add_album),
    path('<str:name>/', about),
    path('<str:name>/<int:number>/', song, name='song_details'),
]