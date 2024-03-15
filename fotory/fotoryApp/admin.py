from django.contrib import admin
from .models import Album, Person, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Başlangıçta gösterilecek boş `Photo` form sayısı

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]
    list_display = ['name', 'description', 'album']
    search_fields = ['name', 'album__name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_type', 'name', 'date_range', 'group_name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['person', 'photo']
    search_fields = ['person__name']
