# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-10 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='学习时长(分钟数)'),
        ),
    ]