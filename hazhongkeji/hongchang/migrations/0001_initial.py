# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-22 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32, null=True, verbose_name='西城红场')),
            ],
            options={
                'verbose_name': '城区名称',
                'verbose_name_plural': '城区名称',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, null=True, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, unique=True, verbose_name='联系方式')),
                ('city', models.CharField(max_length=32, null=True, verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '报名信息',
                'verbose_name_plural': '报名信息',
            },
        ),
    ]
