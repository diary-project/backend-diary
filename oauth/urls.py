from django.urls import path
from .views import kakao_redirect, kakao_login


urlpatterns = [
    path("login/", kakao_redirect, name="kakao_login"),
    path("token/", kakao_login),
]
