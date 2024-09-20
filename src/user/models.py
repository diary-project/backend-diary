from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from common.models import BaseModel
from user.managers import CustomUserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(null=True, max_length=128)
    nickname = models.CharField(max_length=8, unique=False)
    kakao_oid = models.CharField(max_length=200, null=True, unique=True, blank=True)

    is_staff = models.BooleanField(default=False)  # 슈퍼유저 권한
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # 계정 활성화 상태

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
