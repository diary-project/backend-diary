from django.urls import path
from image.views import ImageCreateUpdateAPIView


urlpatterns = [path("", ImageCreateUpdateAPIView.as_view())]
