from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)
    default_address = models.CharField(max_length=100, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    wish_list = models.TextField(null=True, blank=True)
    uid_naver = models.CharField(max_length=50, null=True, blank=True)
    uid_kakao = models.CharField(max_length=50, null=True, blank=True)
    uid_google = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
