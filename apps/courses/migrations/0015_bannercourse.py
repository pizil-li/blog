# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-21 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
            },
            bases=('courses.course',),
        ),
    ]
