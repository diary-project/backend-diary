from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def setUp(self):
        email_to_create = "rlaeowjd2012@gmail.com"
        kakako_oid_to_create = 4324312
        nickname_to_create = "hello"

        User.objects.create(
            email=email_to_create,
            nickname=nickname_to_create,
            kakao_oid=kakako_oid_to_create,
        )

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

    def test_get_user(self):
        email_to_search = "rlaeowjd2012@gmail.com"
        # 단일 객체를 조회할 때
        try:
            user = User.objects.get(email=email_to_search)
        except User.DoesNotExist:
            print("사용자를 찾을 수 없습니다.")
        except User.MultipleObjectsReturned:
            print("여러 개의 사용자가 존재합니다.")
