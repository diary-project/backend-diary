from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.request_serializers import (RequestFullDiarySerializer,
                                              RequestDiaryCreateSerializer,
                                              RequestDiaryUpdateSerializer,
                                              RequestDiaryDeleteSerializer)
from .serializers.response_serializers import (ResponseDiaryDateSerializer,
                                               ResponseFullDiarySerializer,
                                               ResponseCreateDiarySerializer,
                                               ResponseUpdateDiarySerializer)

from .services import (get_diary, get_diary_date_by_year_month,
                       create_diary, update_diary, delete_diary)


class DiaryRetrieveUpdateDeleteAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a diary entry by date",
        responses={200: ResponseFullDiarySerializer()},
        manual_parameters=[
            openapi.Parameter('date', openapi.IN_PATH, description="Date of the diary", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, date: str):
        diary = get_diary(user_id=request.user.id, date=date)
        serializer = ResponseFullDiarySerializer(diary)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update a diary entry by date",
        request_body=RequestDiaryUpdateSerializer,
        responses={200: ResponseUpdateDiarySerializer()},
        manual_parameters=[
            openapi.Parameter('date', openapi.IN_PATH, description="Date of the diary", type=openapi.TYPE_STRING)
        ]
    )
    def put(self, request, date: str):
        content = request.data.get("content", None)
        weather = request.data.get("weather", None)

        data = {
            "date": date,
            "content": content,
            "weather": weather
        }

        serializer = RequestDiaryUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        updated_diary = update_diary(user=request.user, date=date, content=content, weather=weather)
        updated_diary_serializer = ResponseUpdateDiarySerializer(instance=updated_diary)

        return Response(data=updated_diary_serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a diary entry by date",
        responses={204: 'No Content'},
        manual_parameters=[
            openapi.Parameter('date', openapi.IN_PATH, description="Date of the diary", type=openapi.TYPE_STRING)
        ]
    )
    def delete(self, request, date: str):
        delete_diary(user=request.user, date=date)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DiaryDateListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="List all diary entries for a specific year and month",
        responses={200: ResponseDiaryDateSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, description="Year of the diary entries", type=openapi.TYPE_STRING),
            openapi.Parameter('month', openapi.IN_QUERY, description="Month of the diary entries", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            return Response({"error": "Year and month are required."}, status=status.HTTP_400_BAD_REQUEST)

        diary_query_set = get_diary_date_by_year_month(user_id=request.user.id, year=year, month=month)
        data = {"dates": list(diary_query_set.values_list("date", flat=True))}

        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new diary entry",
        request_body=RequestDiaryCreateSerializer,
        responses={201: ResponseCreateDiarySerializer()},
    )
    def post(self, request):
        content = request.data.get("content")
        weather = request.data.get("weather")

        data = {
            "content": content,
            "weather": weather
        }

        serializer = RequestDiaryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        created_diary = create_diary(user=request.user, content=content, weather=weather)
        created_diary_serializer = ResponseCreateDiarySerializer(instance=created_diary)

        return Response(data=created_diary_serializer.data, status=status.HTTP_201_CREATED)


# class DiaryDateListAPIView(APIView):
#     def get(self, request, year: int, month: int):
#         diary_query_set = get_diary_date_by_year_month(user_id=request.user.id, year=year, month=month)
#         diary_date_serializer = ResponseDiaryDateSerializer(data=diary_query_set, many=True)
#
#         return Response(data=diary_date_serializer.data, status=status.HTTP_200_OK)
#
#
# class DiaryAPIView(APIView):
#     def get(self, request, date: str):
#         data = {"date": date}
#         request_full_diary_serializer = RequestFullDiarySerializer(data=data)
#         request_full_diary_serializer.is_valid()
#
#         diary = get_diary(user_id=request.user.id, date=request_full_diary_serializer.data["date"])
#         response_full_diary_serializer = ResponseFullDiarySerializer(instance=diary)
#
#         return Response(data=response_full_diary_serializer.data, status=status.HTTP_200_OK)
#
#
#
#
#
# class DiaryUpdateAPIVIew(APIView):
#     def update(self, request, date: str):
#         content = request.data.get("content", None)
#         weather = request.data.get("weather", None)
#
#         data = {
#             "date": date,
#             "content": content,
#             "weather": weather
#         }
#
#         serializer = RequestDiaryUpdateSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#
#         updated_diary = update_diary(user=request.user, date=date, content=content, weather=weather)
#         updated_diary_serializer = ResponseUpdateDiarySerializer(instance=updated_diary)
#
#         return Response(data=updated_diary_serializer.data, status=status.HTTP_200_OK)
#
#
# class DiaryDeleteAPIView(APIView):
#     def delete(self, request, date: str):
#         data = {"date": date}
#         serializer = RequestDiaryDeleteSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#
#         delete_diary(user=request.user, date=date)
#
#         return Response(status=status.HTTP_200_OK)


# class DiaryListAPIView(generics.ListAPIView):
#     serializer_class = DiaryDateSerializer
#
#     def get_queryset(self):
#         today = timezone.now()
#         user = self.request.user
#
#         # GET 요청에서 연도와 월을 가져옵니다. 없으면 기본값으로 현재 연도와 월을 사용합니다.
#         year = self.request.query_params.get("year", today.year)
#         month = self.request.query_params.get("month", today.month)
#
#         return Diary.objects.filter(user=user, date__year=year, date__month=month)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class DiaryCreateAPIView(generics.CreateAPIView):
#     serializer_class = DiaryCreateUpdateSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class DiaryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Diary.objects.all()
#     serializer_class = DiaryCombinedSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = "date"
#
#     def get_serializer_class(self):
#         if self.request.method == "PUT":
#             return DiaryUpdateSerializer
#         return DiaryCombinedSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return super().get_queryset().filter(user=user)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
