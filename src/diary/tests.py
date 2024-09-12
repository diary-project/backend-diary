from django.test import TestCase
from django.utils import timezone

from diary.services import create_diary, update_diary, delete_diary, get_diary, get_diary_date_by_year_month

from diary.models import Diary
from image.models import Image
from user.models import User
from tag.models import Tag


class DiaryServiceTestCase(TestCase):

    def setUp(self):
        """
        Given: 일기를 작성할 유저와 일기, 태그, 이미지를 생성합니다.
        """
        # 유저 생성
        self.user = User.objects.create_user(
            email="testuser@example.com",
            kakao_oid="hellokakao",
            nickname="testuser"
        )

        # Diary 생성
        self.diary = Diary.objects.create(
            user=self.user,
            content="오늘의 일기",
            weather="sunny",
            # date=timezone.now().date()
        )

        # Tag 생성
        self.tag1 = Tag.objects.create(
            word="태그1",
            diary=self.diary
        )
        self.tag2 = Tag.objects.create(
            word="태그2",
            diary=self.diary
        )

        # Image 생성
        self.image = Image.objects.create(
            prompt="이미지 생성에 사용된 프롬프트",
            url="http://example.com/image.jpg",
            diary=self.diary
        )

    # def test_create_diary(self):
    #     """
    #     When: 새로운 일기를 생성할 때,
    #     Then: 일기가 정상적으로 생성되어야 합니다.
    #     """
    #     new_diary = create_diary(
    #         user=self.user,
    #         content="새로운 일기 내용",
    #         weather="rainy"
    #     )
    #     self.assertIsNotNone(new_diary)
    #     self.assertEqual(new_diary.content, "새로운 일기 내용")
    #     self.assertEqual(new_diary.weather, "rainy")
    #     self.assertEqual(new_diary.user, self.user)

    def test_update_diary(self):
        """
        When: 기존의 일기 내용을 수정할 때,
        Then: 일기의 내용과 날씨가 정상적으로 수정되어야 합니다.
        """
        updated_diary = update_diary(
            user=self.user,
            date=self.diary.date,
            content="수정된 일기 내용",
            weather="cloudy"
        )
        self.assertIsNotNone(updated_diary)
        self.assertEqual(updated_diary.content, "수정된 일기 내용")
        self.assertEqual(updated_diary.weather, "cloudy")

    def test_delete_diary(self):
        """
        When: 일기를 삭제할 때,
        Then: 해당 일기가 정상적으로 삭제되어야 합니다.
        """
        delete_diary(user=self.user, date=self.diary.date)
        with self.assertRaises(Diary.DoesNotExist):
            get_diary(user_id=self.user.id, date=self.diary.date)

    def test_get_diary_date_by_year_month(self):
        """
        When: 특정 년도와 월로 일기를 조회할 때,
        Then: 해당 기간의 일기들이 정상적으로 반환되어야 합니다.
        """
        diaries = get_diary_date_by_year_month(user_id=self.user.id, year=self.diary.date.year, month=self.diary.date.month)
        self.assertEqual(len(diaries), 1)
        self.assertEqual(diaries[0].content, self.diary.content)
        self.assertEqual(diaries[0].tags.count(), 2)  # 태그 개수 확인
        self.assertEqual(diaries[0].image.url, "http://example.com/image.jpg")  # 이미지 URL 확인