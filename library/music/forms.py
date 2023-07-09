from django import forms
from .models import Album
class AddAlbumForm(forms.Form):
    name = forms.CharField(label="Album name", max_length=100)
    artist = forms.CharField(label="Artist name", max_length=100)
    type = forms.CharField(max_length=5)
    songs = forms.IntegerField(min_value=0, max_value=50)
    year_of_publish = forms.IntegerField(min_value=0, max_value=2050)
    image = forms.ImageField(required=False)
    is_borrowed = forms.BooleanField(required=False)

class EditSongForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 30, 'cols': 142}), label='lyrics')
class AddSongForm(forms.Form):
    name = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))