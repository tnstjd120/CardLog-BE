from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10, help_text="이름")
    email = models.CharField(max_length=50, help_text="이메일")
    password = models.CharField(max_length=20, help_text="비밀번호")
    profile_img = models.CharField(max_length=255, help_text="프로필 이미지")
    about = models.CharField(max_length=50, help_text="내 소개")
    blog_name = models.CharField(max_length=20, help_text="블로그 이름")
    access_level = models.BooleanField(default=True, help_text="접근 권한 - True: 접속 가능 / False: 접속 불가")
    create_at = models.DateTimeField(auto_now_add=True, help_text="생성 일자")

    class Meta:
        db_table = 'user'

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
    post_type = models.IntegerField(default=0, help_text="0: 일반 게시물, 100: 카드 게시물")
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