from django.urls import path
from .views import ImageCreateUpdateAPIView


urlpatterns = [path("", ImageCreateUpdateAPIView.as_view())]
