from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from accounts.models import User

class LinkList(models.Model):
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE)
    icon_type = models.IntegerField(default=0, help_text="0: Github / 1: blog -> 추후 업데이트 예정")
    url = models.CharField(max_length=255, help_text="링크 url")

    class Meta:
        db_table = 'link_list'

class Category(models.Model):
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, help_text="카테고리 이름")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'category'

class Post(models.Model):
    category = models.ForeignKey(Category, default=1, blank=True, null=True, on_delete=models.CASCADE)
    post_type = models.IntegerField(default=0, help_text="0: 일반 게시물, 1: 카드 게시물")
    title = models.CharField(max_length=50, help_text="게시물 제목")
    content = models.TextField(help_text="게시물 내용")
    bg_color = models.CharField(max_length=10, default='#FFFFFF', help_text="카드 배경색 (HEX)")
    text_color = models.CharField(max_length=10, default='#333333', help_text="카드 글자색 (HEX)")
    thumbnail = models.CharField(max_length=255, default='', help_text="게시글 썸네일")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'post'

class PostLike(models.Model):
    post = models.ForeignKey(Post, default=1, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE, help_text="게시물 좋아요한 유저")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'post_like'

class Comment(models.Model):
    post = models.ForeignKey(Post, default=1, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE, help_text="댓글 작성 유저")
    content = models.TextField(help_text="댓글 내용")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'comment'

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, default=1, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE, help_text="댓글 좋아요한 유저")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'comment_like'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, default=1, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE, help_text="답글 작성 유저")
    content = models.TextField(help_text="답글 내용")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'reply'

class ReplyLike(models.Model):
    reply = models.ForeignKey(Reply, default=1, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.CASCADE, help_text="답글 좋아요한 유저")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")
    update_at = models.DateTimeField(auto_now=True, help_text="수정 일자")

    class Meta:
        db_table = 'reply_like'