# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-31 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhizhu_proxy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32, verbose_name='城区')),
            ],
            options={
                'verbose_name': '城区名称',
                'verbose_name_plural': '城区名称',
            },
        ),
        migrations.CreateModel(
            name='Wangba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wb', models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='zhizhu_proxy.City', verbose_name='网吧')),
            ],
            options={
                'verbose_name': '网吧名称',
                'verbose_name_plural': '网吧名称',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=32, null=True, verbose_name='城区'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='wb',
            field=models.CharField(max_length=32, null=True, verbose_name='网吧'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=32, unique=True, verbose_name='联系方式'),
        ),
    ]