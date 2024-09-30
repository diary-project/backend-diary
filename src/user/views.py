from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserNicknameSerializer
from utils.log_utils import Logger


class UserNicknameMixinAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserNicknameSerializer

    def get(self, request, *args, **kwargs):
        user_email = request.user.email
        user = User.objects.get(email=user_email)
        data = {"nickname": user.nickname}
        Logger.debug(f"UserNicknameMixinAPIView.get - data : {data}")

        return Response(data=data, status=status.HTTP_200_OK)


class UserNicknameAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_email = user.email

        user = User.objects.get(email=user_email)
        return Response(data={"nickname": user.nickname}, status=status.HTTP_200_OK)
