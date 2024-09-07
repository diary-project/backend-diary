from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, nickname=None, kakao_oid=None, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("이메일 필드가 작성되어야 합니다.")

        # 이메일을 표준 형식으로 변환
        email = self.normalize_email(email)
        user = self.model(
            email=email, nickname=nickname, kakao_oid=kakao_oid, **extra_fields
        )
        user.set_password(password)  # 비밀번호 설정
        user.save(using=self._db)  # 저장
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # 슈퍼유저는 항상 is_staff와 is_superuser가 True여야 합니다.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # 필수값 검증
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser는 is_staff=True여야 합니다.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser는 is_superuser=True여야 합니다.")

        # 슈퍼유저 생성 시 nickname이 필수면 기본값을 설정해줍니다.
        if "nickname" not in extra_fields:
            extra_fields["nickname"] = "admin"

        return self.create_user(email, password=password, **extra_fields)
