from rest_framework import serializers
from .models import Image


class ImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["url"]


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "prompt"]
