from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from oauth.views import KakaoRedirectView, KakaoLoginView

urlpatterns = [
    path("login/", KakaoRedirectView.as_view()),
    path("token/", KakaoLoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("verify/", TokenVerifyView.as_view()),
]
