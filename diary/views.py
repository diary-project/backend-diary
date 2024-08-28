from datetime import datetime

from django.core.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from .serializers import DiaryDateSerializer, DiaryDetailSerializer, DiaryCreateSerializer, DiaryUpdateSerializer
from .models import Diary


class DiariesMixinAPIView(generics.ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryDateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DiaryCreateMixinAPIView(generics.CreateAPIView):
    serializer_class = DiaryCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DiaryMixinAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSerializer
    lookup_field = 'date'

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return DiaryUpdateSerializer
        return DiaryDetailSerializer

    def get_object(self):
        # 쿼리 파라미터에서 'date' 값을 가져옵니다.
        date_str = self.request.query_params.get('date')

        if not date_str:
            raise ValidationError("Date query parameter is required.")

        # date_str을 DateField로 변환합니다.
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

        # 변환된 date_obj로 객체를 조회합니다.
        return get_object_or_404(self.queryset, date=date_obj)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
