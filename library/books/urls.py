from django.urls import path, include
from .views import index, add_book

urlpatterns = [
    path('', index),
    path('add/', add_book)
]