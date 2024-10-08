from django.db import transaction
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from user.models import User
from user.serializers import UserNicknameSerializer
from utils.log_utils import Logger


class UserNicknameAPIView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserNicknameSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        data = {"nickname": user.nickname}
        Logger.debug(f"UserNicknameAPIView.get - data : {data}")

        return Response(data=data, status=status.HTTP_200_OK)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {"nickname": user.nickname}
        Logger.debug(f"UserNicknameAPIView.update - data : {data}")

        return Response(data=data, status=status.HTTP_200_OK)
