from django.urls import path
from diary.views import DevDiaryCreateView

urlpatterns = [
    path("", DevDiaryCreateView.as_view(), name="diary-dev"),
]
