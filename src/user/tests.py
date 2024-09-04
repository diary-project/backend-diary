from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def test_create_user(self):
        email = "test@test.com"
        nickname = "testtest"
        kakao_oid = "123124"

        user, create = User.objects.get_or_create(
            email=email,
            defaults={
                "nickname": nickname,
                "kakao_oid": kakao_oid,
            },
        )

        print("생성 여부 :", create)
        print("사용자 정보 :", user)
