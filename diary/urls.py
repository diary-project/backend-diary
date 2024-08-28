from django.urls import path
from .views import DiaryMixinAPIView, DiariesMixinAPIView, DiaryCreateMixinAPIView

urlpatterns = [
    path('add/', DiaryCreateMixinAPIView.as_view()),
    path('detail/', DiaryMixinAPIView.as_view()),
    path('', DiariesMixinAPIView.as_view()),
]
