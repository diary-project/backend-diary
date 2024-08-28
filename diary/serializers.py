from rest_framework import serializers

from .models import Diary


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
