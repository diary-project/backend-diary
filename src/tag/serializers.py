from rest_framework import serializers
from tag.models import Tag


class TagWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["word"]


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["word", "diary"]


class TagUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["word"]
