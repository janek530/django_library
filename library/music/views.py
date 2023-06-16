from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Album, Song
from .forms import AddAlbumForm, AddSongForm
import re

# Create your views here.
def index(request):
    albums = Album.objects.all()
    try:
        sort = request.GET['sort']
        albums = albums.order_by(sort)
        return render(request, 'index.html', {'albums': albums})
    except:
        return render(request, 'index.html', {'albums': albums})

def about(request, name):
    album = Album.objects.get(name=name)
    album_id = album.id
    print(album_id)
    songs = album.song_set.all()
    track_num = len(songs)+1
    if request.method == "POST":
        form = AddSongForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            text = form.cleaned_data['text']
            song = Song(album=album, name=n, track_number=track_num, text=text)
            song.save()
            return HttpResponseRedirect("")
    else:
        form = AddSongForm()
    return render(request, 'about.html', {'album': album, 'songs': songs, 'count_song': len(songs), 'song_form': form})

def song(request, name, number):
    album = Album.objects.get(name=name)
    songs = album.song_set.all()
    song = songs.get(track_number=number)
    lyrics = re.split('\[.*]', song.text)
    nums_of_songs = album.songs
    next = song.track_number + 1
    previous = song.track_number - 1
    context = {
        'album': album,
        'song': song,
        'nums_of_songs': nums_of_songs,
        'next': next,
        'previous': previous,
        'lyrics': lyrics
    }
    return render(request, 'song.html', context)

def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['artist']
            t = form.cleaned_data['type']
            s = form.cleaned_data['songs']
            yop = form.cleaned_data['year_of_publish']
            image = form.cleaned_data['image']
            ib = form.cleaned_data['is_borrowed']
            a = Album(name=n, artist=a, type=t, songs=s, year_of_publish=yop, image=image, is_borrowed = ib)
            a.save()
            return HttpResponseRedirect("")
    else:
        form = AddAlbumForm()
    return render(request, 'add.html', {'form': form})