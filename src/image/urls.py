from django.urls import path
from .views import ImageCreateUpdateMixinAPIView


urlpatterns = [path("", ImageCreateUpdateMixinAPIView.as_view())]
