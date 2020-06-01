from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    GENDER = (
        ("M", "남자"),
        ("F", "여자"),
    )
 # 둘다 트루인경우 -- 로그인에 상관 ㄴㄴ
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True, choices=GENDER)
