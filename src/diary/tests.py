# tests.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from user.models import User
from diary.models import Diary
from image.models import Image
from tag.models import Tag


class DiaryAPITestCase(APITestCase):
    def setUp(self):
        # 테스트 사용자 생성
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            nickname='testnickname'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # 로그인한 상태로 설정

        # 테스트 일기 생성
        self.diary = Diary.objects.create(
            date=timezone.now().date(),
            content='오늘 하루는 정말 좋았어!',
            user=self.user
        )

        # 이미지와 태그 추가
        self.image = Image.objects.create(
            prompt='A beautiful scenery',
            url='https://example.com/scenery.jpg',
            diary=self.diary
        )

        self.tag = Tag.objects.create(
            word='행복',
            diary=self.diary
        )

    def test_get_diary_list(self):
        """
        로그인된 사용자가 자신의 모든 일기를 조회하는 테스트
        """
        url = reverse('diary-list')
        response = self.client.get(url)

        # 응답 상태 코드가 200인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 반환된 일기 목록에 테스트 일기가 포함되는지 확인
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], '오늘 하루는 정말 좋았어!')

    def test_get_diary_detail(self):
        """
        특정 날짜의 일기와 해당 일기에 연결된 이미지와 태그를 조회하는 테스트
        """
        url = reverse('diary-detail', args=[self.diary.date])
        response = self.client.get(url)

        # 응답 상태 코드가 200인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 반환된 일기 내용이 올바른지 확인
        self.assertEqual(response.data['content'], '오늘 하루는 정말 좋았어!')

        # 이미지와 태그가 포함되어 있는지 확인
        self.assertEqual(response.data['image']['url'], 'https://example.com/scenery.jpg')
        self.assertEqual(response.data['tags'][0]['word'], '행복')

    def test_unauthorized_access(self):
        """
        비로그인 상태에서 일기를 조회할 경우 401 응답을 확인하는 테스트
        """
        self.client.logout()  # 로그아웃 처리
        url = reverse('diary-list')
        response = self.client.get(url)

        # 응답 상태 코드가 401인지 확인 (인증되지 않음)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)