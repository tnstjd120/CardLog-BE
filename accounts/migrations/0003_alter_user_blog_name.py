# Generated by Django 4.1.7 on 2023-03-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='blog_name',
            field=models.CharField(default='CardLog', help_text='블로그 이름', max_length=20),
        ),
    ]