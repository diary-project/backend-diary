from rest_framework import serializers
from .models import Tag


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["word", "diary"]


class TagUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["word"]
