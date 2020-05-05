from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "url", "caption", "details"]
        model = Photo
