# Generated by Django 4.1.7 on 2023-03-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blog_id',
            field=models.CharField(blank=True, help_text='블로그 아이디', max_length=20, null=True),
        ),
    ]
