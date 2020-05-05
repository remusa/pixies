from rest_framework import generics

from .models import Photo
from .serializers import PhotoSerializer


class PhotosListView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
