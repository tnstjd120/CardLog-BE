# Generated by Django 4.1.7 on 2023-03-07 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bg_color',
            field=models.CharField(default='#FFFFFF', help_text='카드 배경색 (HEX)', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='text_color',
            field=models.CharField(default='#333333', help_text='카드 글자색 (HEX)', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(default='', help_text='게시글 썸네일', max_length=255),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.AlterModelTable(
            name='commentlike',
            table='comment_like',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postlike',
            table='post_like',
        ),
        migrations.AlterModelTable(
            name='reply',
            table='reply',
        ),
        migrations.AlterModelTable(
            name='replylike',
            table='reply_like',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.CreateModel(
            name='LinkList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_type', models.IntegerField(default=0, help_text='0: Github / 1: blog -> 추후 업데이트 예정')),
                ('url', models.CharField(help_text='링크 url', max_length=255)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'link_list',
            },
        ),
    ]
