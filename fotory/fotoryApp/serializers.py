from rest_framework import serializers
from .models import Album, Person, Photo, GroupPhoto, JointPhoto

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class PersonSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('name', 'description', 'profile_photo', 'photos')


class GroupPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPhoto
        fields = ('photo',)

class JointPhotoSerializer(serializers.ModelSerializer):
    people = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = JointPhoto
        fields = ('photo', 'people')

class AlbumSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True, read_only=True)
    group_photos = GroupPhotoSerializer(many=True, read_only=True)
    joint_photos = JointPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'album_type', 'date_range', 'group_name', 'persons', 'group_photos', 'joint_photos')
