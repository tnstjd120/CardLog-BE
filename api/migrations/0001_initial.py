# Generated by Django 4.1.7 on 2023-03-15 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, help_text='이름', max_length=10, null=True)),
                ('email', models.EmailField(help_text='이메일', max_length=30, unique=True)),
                ('profile_img', models.CharField(blank=True, help_text='프로필 이미지', max_length=255, null=True)),
                ('about', models.CharField(blank=True, help_text='내 소개', max_length=50, null=True)),
                ('blog_name', models.CharField(blank=True, help_text='블로그 이름', max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='접근 권한 - True: 접속 가능 / False: 접속 불가')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='카테고리 이름', max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='댓글 내용')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.IntegerField(default=0, help_text='0: 일반 게시물, 1: 카드 게시물')),
                ('title', models.CharField(help_text='게시물 제목', max_length=50)),
                ('content', models.TextField(help_text='게시물 내용')),
                ('bg_color', models.CharField(default='#FFFFFF', help_text='카드 배경색 (HEX)', max_length=10)),
                ('text_color', models.CharField(default='#333333', help_text='카드 글자색 (HEX)', max_length=10)),
                ('thumbnail', models.CharField(default='', help_text='게시글 썸네일', max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='답글 내용')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('comment', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.comment')),
                ('user', models.ForeignKey(blank=True, default=1, help_text='답글 작성 유저', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reply',
            },
        ),
        migrations.CreateModel(
            name='ReplyLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('reply', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.reply')),
                ('user', models.ForeignKey(blank=True, default=1, help_text='답글 좋아요한 유저', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reply_like',
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('post', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.post')),
                ('user', models.ForeignKey(blank=True, default=1, help_text='게시물 좋아요한 유저', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post_like',
            },
        ),
        migrations.CreateModel(
            name='LinkList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_type', models.IntegerField(default=0, help_text='0: Github / 1: blog -> 추후 업데이트 예정')),
                ('url', models.CharField(help_text='링크 url', max_length=255)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'link_list',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성 일자')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정 일자')),
                ('comment', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.comment')),
                ('user', models.ForeignKey(blank=True, default=1, help_text='댓글 좋아요한 유저', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment_like',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, default=1, help_text='댓글 작성 유저', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
