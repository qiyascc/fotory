
from django.test import TestCase
from fotoryApp.serializers import AlbumSerializer
from .models import Album, Person, Photo, GroupPhoto, JointPhoto
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

# Testing Models
class ModelTests(TestCase):
    def test_create_album(self):
        album = Album.objects.create(
            album_type='education',
            name='Test Album',
            date_range='2020-2024',
            group_name='Test Group'
        )
        self.assertEqual(str(album), 'Education - Test Album - Test Group')

    def test_create_person(self):
        album = Album.objects.create(
            album_type='education',
            name='Test Album',
            date_range='2020-2024',
            group_name='Test Group'
        )
        person = Person.objects.create(
            album=album,
            name='Qiyas CC',
            description='A Super Person'
        )
        self.assertEqual(str(person), 'Qiyas CC - Test Album')


# Testing Views
class ViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_album_list_access_denied_without_key(self):
        response = self.client.get(reverse('album-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_album_list_access_granted_with_key(self):
        self.client.credentials(HTTP_ACCESS_KEY='qiyascc')
        response = self.client.get(reverse('album-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)




