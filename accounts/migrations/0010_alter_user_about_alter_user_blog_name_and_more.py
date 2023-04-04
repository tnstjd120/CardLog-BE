# Generated by Django 4.1.7 on 2023-04-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, db_collation='utf8mb4_unicode_ci', default='내 정보에서 내 소개를 입력해서 변경해주세요!', help_text='내 소개', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='blog_name',
            field=models.CharField(default='카드로그 제목', help_text='블로그 이름', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='blog_url',
            field=models.CharField(blank=True, default='', help_text='blog url', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='github_url',
            field=models.CharField(blank=True, default='', help_text='github url', max_length=255, null=True),
        ),
    ]
