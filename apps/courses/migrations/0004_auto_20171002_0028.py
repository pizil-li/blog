# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-02 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20171002_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='click_nums',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='点击数'),
        ),
    ]
