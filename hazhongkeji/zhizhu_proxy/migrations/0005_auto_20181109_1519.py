# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-09 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhizhu_proxy', '0004_auto_20181106_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=32, null=True, verbose_name='城区'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, null=True, verbose_name='姓名'),
        ),
    ]
