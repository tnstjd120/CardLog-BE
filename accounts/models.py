from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, null=True, blank=True, help_text="이름")
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False, help_text="이메일")
    password = models.CharField(max_length=255, help_text="비밀번호")
    profile_img = models.CharField(max_length=255, default="", help_text="프로필 이미지")
    about = models.TextField(null=True, blank=True, default="내 정보에서 내 소개를 입력해서 변경해주세요!", db_collation='utf8mb4_unicode_ci', help_text="내 소개")
    phone = models.CharField(max_length=13, null=True, blank=True, help_text="핸드폰 번호")
    blog_id = models.CharField(max_length=20, null=True, blank=True, unique=True, help_text="블로그 아이디")
    blog_name = models.CharField(max_length=20, default="카드로그 제목", help_text="블로그 이름")
    
    github_url = models.CharField(max_length=255, null=True, blank=True, default="", help_text="github url")
    blog_url = models.CharField(max_length=255, null=True, blank=True, default="", help_text="blog url")

    is_active = models.BooleanField(default=True, help_text="접근 권한 - True: 접속 가능 / False: 접속 불가")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email