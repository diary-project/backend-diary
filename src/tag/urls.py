from django.urls import path
from tag.views import TagCreateUpdateMixinAPIView


urlpatterns = [path("", TagCreateUpdateMixinAPIView.as_view())]
