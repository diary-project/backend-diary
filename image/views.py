from rest_framework import generics
from .serializers import ImageCreateSerializer, ImageUpdateSerializer


class ImageCreateUpdateMixinAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ImageCreateSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ImageUpdateSerializer
        return ImageCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
