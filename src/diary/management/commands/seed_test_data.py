# myapp/management/commands/create_test_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from user.models import User
from diary.models import Diary
from image.models import Image
from tag.models import Tag


class Command(BaseCommand):
    help = "Create test data for development"

    def handle(self, *args, **kwargs):
        # CustomUserManager의 create_user 메서드 활용
        user, created = User.objects.get_or_create(
            email="test@example.com",
            defaults={
                "nickname": "TestUser",
                "password": "test1234",  # 비밀번호는 암호화되어 저장됨
            },
        )

        if created:
            user.set_password("test1234")  # 비밀번호 암호화 저장
            user.save()

        # 다이어리 생성
        diary, created = Diary.objects.get_or_create(
            date=timezone.now().date(),
            user=user,
            defaults={
                "content": "오늘은 테스트 데이터를 작성했습니다.",
            },
        )

        # 이미지 생성
        Image.objects.get_or_create(
            diary=diary,
            defaults={
                "prompt": "테스트 이미지",
                "url": "http://example.com/image.jpg",
            },
        )

        # 태그 생성
        Tag.objects.get_or_create(
            word="테스트태그",
            diary=diary,
        )

        self.stdout.write(self.style.SUCCESS("Successfully created test data!"))
