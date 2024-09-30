from rest_framework import serializers
from diary.models import Diary
from utils.date_utils import DateUtil


class RequestDiaryCreateSerializer(serializers.ModelSerializer):
    """
    일기 생성에 활용하는 Serializer
    [POST] /diary/
    """

    class Meta:
        model = Diary
        fields = ["user", "content", "weather"]

    def validate(self, attrs):
        print(attrs)

        if "content" not in attrs or "weather" not in attrs:
            raise serializers.ValidationError("content, weather 필드는 필수입니다.")

        if Diary.objects.filter(user=attrs["user"], date=DateUtil.get_today()).exists():
            raise serializers.ValidationError("오늘 일기는 이미 작성되었습니다.")

        return attrs


class RequestDevDiaryCreateSerializer(serializers.ModelSerializer):
    """
    일기 생성에 활용하는 Serializer
    [POST] /diary/
    """

    class Meta:
        model = Diary
        fields = ["user", "date", "content", "weather"]

    def validate(self, attrs):
        if "content" not in attrs or "weather" not in attrs:
            raise serializers.ValidationError("content, weather 필드는 필수입니다.")

        if Diary.objects.filter(user=attrs["user"], date=attrs["date"]).exists():
            raise serializers.ValidationError("오늘 일기는 이미 작성되었습니다.")

        return attrs


class RequestDiaryUpdateSerializer(serializers.ModelSerializer):
    """
    일기 수정에 활용하는 Serializer
    [PUT, PATCH] /diary/<date:str>
    """

    class Meta:
        model = Diary
        fields = ["user", "date", "content", "weather"]


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
