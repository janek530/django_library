from django.urls import path, include
from .views import index, add_book, book_details

urlpatterns = [
    path('', index),
    path('add/', add_book),
    path('<str:title>/', book_details)
]