from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Album

class AlbumAPITests(APITestCase):
    def setUp(self):
        Album.objects.create(album_type='education', name='Test Album', date_range='2020-2024', group_name='Test Group')

    def test_get_albums_with_access_key(self):
        url = reverse('album-list')
        response = self.client.get(url, HTTP_ACCESS_KEY='qiyascc')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Album')
