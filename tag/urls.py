from django.urls import path
from .views import TagCreateUpdateMixinAPIView


urlpatterns = [
    path('', TagCreateUpdateMixinAPIView.as_view())
]
