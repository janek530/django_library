from django import forms
from .models import Book

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.CharField(max_length=150)
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))