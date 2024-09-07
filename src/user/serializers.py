from rest_framework import serializers
from .models import User


class UserNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname"]
