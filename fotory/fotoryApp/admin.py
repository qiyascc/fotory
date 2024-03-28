from django.contrib import admin
from .models import Album, Person, Photo, GroupPhoto, JointPhoto

class BasePhotoInline(admin.TabularInline):
    extra = 1
    model = None

class PhotoInline(BasePhotoInline):
    model = Photo

class GroupPhotoInline(BasePhotoInline):
    model = GroupPhoto
    

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description', 'album')
    search_fields = ('name', 'album__name')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('person', 'photo')
    search_fields = ('person__name',)

@admin.register(GroupPhoto)
class GroupPhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'photo')
    search_fields = ('album__name',)

@admin.register(JointPhoto)
class JointPhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'photo_display')
    search_fields = ('album__name',)
    filter_horizontal = ('people',)

    def photo_display(self, obj):
        people_names = [person.name for person in obj.people.all()]
        return ', '.join(people_names) if people_names else 'No people listed'
    photo_display.short_description = 'People in Photo'

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [GroupPhotoInline]
    list_display = ('album_type', 'name', 'date_range', 'group_name')
