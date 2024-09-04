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
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Diary
        fields = ['date', 'content', 'url', 'tags']

    def get_tags(self, obj):
        tags = Tag.objects.filter(diary=obj)
        return [tag.word for tag in tags]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        try:
            image = Image.objects.get(diary=instance)
            representation['url'] = image.url
        except Image.DoesNotExist:
            representation['url'] = None

        representation['tags'] = self.get_tags(instance)

        return representation
