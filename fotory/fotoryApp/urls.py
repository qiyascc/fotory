from django.urls import path
from .views import AlbumList

urlpatterns = [
    path('albums/', AlbumList.as_view(), name='album-list'),
]
