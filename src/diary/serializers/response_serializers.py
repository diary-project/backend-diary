from rest_framework import serializers

from diary.models import Diary
from image.serializers import ImageUrlSerializer
from tag.serializers import TagWordSerializer


class ResponseDiaryDateSerializer(serializers.ModelSerializer):
    """
    일기 날짜 조회 응답에 활용하는 Serializer
    [GET] /diary/
    {
        "dates": ["2024-08-12", "2024-08-13", ...]
    }
    """
    dates = serializers.SerializerMethodField()

    def get_dates(self, obj):
        return Diary.objects.values_list("date", flat=True)

    class Meta:
        model = Diary
        fields = ["dates"]


class ResponseFullDiarySerializer(serializers.ModelSerializer):
    """
    일기 조회 응답에 활용하는 Serializer
    [GET] /diary/<date:str>
    {
        "date": str
        "content": str
        "weather": str
        "tags": ["hello", "world"]
        "images": ["https://imageurl.com"]
    }
    """
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        tags = obj.tags.all()
        return [tag["word"] for tag in TagWordSerializer(tags, many=True).data]

    def get_images(self, obj):
        urls = obj.images.all()
        return [image["url"] for image in ImageUrlSerializer(urls, many=True).data]

    class Meta:
        model = Diary
        fields = ["date", "content", "weather", "tags", "images"]


class ResponseCreateDiarySerializer(serializers.ModelSerializer):
    """
    일기 생성 응답에 활용하는 Serializer
    [POST] /diary/
    """
    class Meta:
        model = Diary
        exclude = ["user"]


class ResponseUpdateDiarySerializer(serializers.ModelSerializer):
    """
    일기 수정 응답에 활용하는 Serializer
    [PUT, PATCH] /diary/<date:str>
    """
    class Meta:
        model = Diary
        exclude = ["user"]


