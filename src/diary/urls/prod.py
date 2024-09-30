from django.urls import path
from diary.views import DiaryRetrieveUpdateDeleteAPIView, DiaryDateListCreateAPIView

urlpatterns = [
    path("<str:date>/", DiaryRetrieveUpdateDeleteAPIView.as_view(), name="diary-detail"),
    path("", DiaryDateListCreateAPIView.as_view(), name="diary-list"),
]
