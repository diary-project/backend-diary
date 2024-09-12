from rest_framework import serializers
from diary.models import Diary


class RequestDiaryCreateSerializer(serializers.ModelSerializer):
    """
    일기 생성에 활용하는 Serializer
    [POST] /diary/
    """
    class Meta:
        model = Diary
        fields = ["content", "weather"]


class RequestDiaryUpdateSerializer(serializers.ModelSerializer):
    """
    일기 수정에 활용하는 Serializer
    [PUT, PATCH] /diary/<date:str>
    """
    class Meta:
        model = Diary
        fields = ["date", "content", "weather"]


class RequestDiaryDeleteSerializer(serializers.ModelSerializer):
    """
    일기 삭제에 활용하는 Serializer
    [DELETE] /diary/<date:str>
    """
    class Meta:
        model = Diary
        fields = ["date"]


# class RequestDiaryDateSerializer(serializers.Serializer):
#     """
#     일기 날짜들 반환 요청에 활용하는 Serializer
#     [GET] /diary/
#     """
#     year = serializers.IntegerField()
#     month = serializers.IntegerField()


class RequestFullDiarySerializer(serializers.ModelSerializer):
    """
    일기 조회 요청에 활용하는 Serializer
    [GET] /diary/<date:str>
    """
    class Meta:
        model = Diary
        fields = ["date"]
