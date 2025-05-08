from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    file = Base64ImageField()

    class Meta:
        model = Photo
        fields = [
            "image_name",
            "file",
        ]


class PhotoResponseSerializer(serializers.Serializer):
    """
    Используется для drf-spectacular.
    """

    random_int = serializers.IntegerField()
