from django.urls import path

from . import bookViews

urlpatterns = [
    path('books', bookViews.listbooks),
]