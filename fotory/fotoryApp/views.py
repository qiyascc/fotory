from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from .models import Album
from .serializers import AlbumSerializer

class HasAccessKey(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('Access-Key') == 'ur_acces_key'

class AlbumList(APIView):
    permission_classes = [HasAccessKey]

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
