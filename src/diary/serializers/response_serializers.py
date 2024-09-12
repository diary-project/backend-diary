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
    class Meta:
        model = Diary
        fields = ["date"]

    def to_representation(self, instance):
        # instance는 queryset입니다.
        response = super().to_representation(instance)
        dates = [item["date"] for item in response]  # 모든 date만 추출
        return {"date": dates}


class ResponseFullDiarySerializer(serializers.ModelSerializer):
    """
    일기 조회 응답에 활용하는 Serializer
    [GET] /diary/<date:str>
    {
        "date": str
        "content": str
        "weather": str
        "tags": {
            [
                "word": "hello",
                "word": "world"
            ]
        }
    }
    """
    images = ImageUrlSerializer(many=True, read_only=True)
    tags = TagWordSerializer(many=True, read_only=True)

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


