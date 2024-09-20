from django.urls import path
from user.views import UserNicknameMixinAPIView, UserNicknameAPIView


urlpatterns = [
    path("nickname/", UserNicknameMixinAPIView.as_view()),
    path("nickname2/", UserNicknameAPIView.as_view()),
]
