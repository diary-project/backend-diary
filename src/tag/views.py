from rest_framework import generics
from tag.serializers import TagCreateSerializer, TagUpdateSerializer


class TagCreateUpdateMixinAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = TagCreateSerializer

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        """
        if self.request.method == "PUT":
            return TagUpdateSerializer
        return TagCreateSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a tag instance.
        """
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update a tag instance.
        """
        return self.update(request, *args, **kwargs)
