from django.urls import path
from user.views import UserNicknameAPIView


urlpatterns = [
    path(
        "nickname/",
        UserNicknameAPIView.as_view(
            {
                "get": "get",
                "put": "update",
            }
        ),
    ),
]
