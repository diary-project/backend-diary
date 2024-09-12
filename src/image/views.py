from rest_framework import generics, mixins
from .serializers import ImageCreateSerializer, ImageUpdateSerializer


class ImageCreateUpdateAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = ImageCreateSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ImageUpdateSerializer
        return ImageCreateSerializer

    def perform_create(self, serializer):
        # Post에 Diary ID값을 받아오나?
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
