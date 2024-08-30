from rest_framework import serializers

from .models import Diary
from image.models import Image
from tag.models import Tag


class DiaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['content', 'date']


class DiaryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['content']


class DiaryDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['date']


class DiaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"


class DiaryCombinedSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='image.url')
    tags = serializers.ListSerializer(
        child=serializers.CharField(source='tag.word')
    )

    class Meta:
        model = Diary
        fields = ['date', 'content', 'url', 'tags']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        try:
            image = Image.objects.get(diary=instance)
            representation['url'] = image.url
        except Image.DoesNotExist:
            representation['url'] = None

        try:
            tags = Tag.objects.filter(diary=instance)
            tag_list = [tag.word for tag in tags]
            representation['tags'] = tag_list
        except Tag.DoesNotExist:
            representation['tags'] = []

        return representation
