from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from common.responses import create_success_response

from diary.serializers.request_serializers import (
    RequestFullDiarySerializer,
    RequestDiaryCreateSerializer,
    RequestDiaryUpdateSerializer,
    RequestDiaryDeleteSerializer,
    RequestDevDiaryCreateSerializer,
)
from diary.serializers.response_serializers import (
    ResponseDiaryDateSerializer,
    ResponseFullDiarySerializer,
    ResponseCreateDiarySerializer,
    ResponseUpdateDiarySerializer,
)

from diary.services import (
    get_diary,
    get_diary_date_by_year_month,
    create_diary,
    create_diary_dev,
    update_diary,
    delete_diary,
)
from tag.tasks import tag_task
from image.tasks import image_task
from utils.log_utils import Logger


class DiaryRetrieveUpdateDeleteAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a diary entry by date",
        responses={200: ResponseFullDiarySerializer()},
        manual_parameters=[
            openapi.Parameter(
                "date",
                openapi.IN_PATH,
                description="Date of the diary",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, date: str):
        diary = get_diary(user_id=request.user.id, date=date)
        serializer = ResponseFullDiarySerializer(diary)

        Logger.debug(f"DiaryRetrieveUpdateDeleteAPIView - get -> diary : {serializer.data}")
        return create_success_response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update a diary entry by date",
        request_body=RequestDiaryUpdateSerializer,
        responses={200: ResponseUpdateDiarySerializer()},
        manual_parameters=[
            openapi.Parameter(
                "date",
                openapi.IN_PATH,
                description="Date of the diary",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def put(self, request, date: str):
        content = request.data.get("content", None)
        weather = request.data.get("weather", None)
        user_id = request.user.id

        data = {"user": user_id, "date": date, "content": content, "weather": weather}

        serializer = RequestDiaryUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        updated_diary = update_diary(user=request.user, date=date, content=content, weather=weather)
        Logger.debug(f"DiaryRetrieveUpdateDeleteAPIView - put -> updated diary : {updated_diary}")

        updated_diary_serializer = ResponseUpdateDiarySerializer(instance=updated_diary)

        return create_success_response(data=updated_diary_serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a diary entry by date",
        responses={204: "No Content"},
        manual_parameters=[
            openapi.Parameter(
                "date",
                openapi.IN_PATH,
                description="Date of the diary",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def delete(self, request, date: str):
        delete_diary(user=request.user, date=date)
        Logger.debug(f"DiaryRetrieveUpdateDeleteAPIView - delete -> diary deleted : {date}")
        return create_success_response(status=status.HTTP_204_NO_CONTENT)


class DiaryDateListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="List all diary entries for a specific year and month",
        responses={200: ResponseDiaryDateSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "year",
                openapi.IN_QUERY,
                description="Year of the diary entries",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "month",
                openapi.IN_QUERY,
                description="Month of the diary entries",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")

        if not year or not month:
            return create_success_response(
                {"error": "Year and month are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        diary_query_set = get_diary_date_by_year_month(user_id=request.user.id, year=year, month=month)
        data = {"dates": list(diary_query_set.values_list("date", flat=True))}
        Logger.debug(f"DiaryDateListCreateAPIView - get -> diary dates : {data}")

        return create_success_response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new diary entry",
        request_body=RequestDiaryCreateSerializer,
        responses={201: ResponseCreateDiarySerializer()},
    )
    def post(self, request):
        content = request.data.get("content")
        weather = request.data.get("weather")
        user_id = request.user.id

        data = {"user": user_id, "content": content, "weather": weather}

        serializer = RequestDiaryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        created_diary = create_diary(user=request.user, content=content, weather=weather)
        Logger.debug(f"DiaryDateListCreateAPIView - post -> created diary : {created_diary}")

        created_diary_serializer = ResponseCreateDiarySerializer(instance=created_diary)
        return create_success_response(data=created_diary_serializer.data, status=status.HTTP_201_CREATED)


class DevDiaryCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new diary entry for development",
        request_body=RequestDevDiaryCreateSerializer,
        responses={201: ResponseCreateDiarySerializer()},
    )
    def post(self, request):
        user_id = request.user.id
        content = request.data.get("content")
        weather = request.data.get("weather")
        date = request.data.get("date")

        data = {"user": user_id, "content": content, "weather": weather, "date": date}

        serializer = RequestDevDiaryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        created_diary = create_diary_dev(user_id=user_id, content=content, weather=weather, date=date)
        Logger.debug(f"DiaryDateListCreateAPIView - post -> created diary : {created_diary}")

        created_diary_serializer = ResponseCreateDiarySerializer(instance=created_diary)
        return create_success_response(data=created_diary_serializer.data, status=status.HTTP_201_CREATED)
