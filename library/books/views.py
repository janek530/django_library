from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from .forms import AddBookForm
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'book_index.html', {'books': books})

def book_details(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'book_details.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['title']
            a = form.cleaned_data['author']
            d = form.cleaned_data['desc']
            b = Book(title=t, author=a, desc=d)
            b.save()
            return HttpResponseRedirect("")
    else:
        form = AddBookForm()
    return render(request, 'add.html', {'form': form})