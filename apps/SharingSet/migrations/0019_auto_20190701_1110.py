# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-01 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SharingSet', '0018_auto_20180709_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharingsetmodel',
            name='imageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='SharingSet/%y/%d/6c8ed0abc140408c8c2b2e2fdd01f751', verbose_name='分享图片'),
        ),
        migrations.AlterField(
            model_name='sharingsetmodel',
            name='set_path',
            field=models.CharField(choices=[('5', '内容页面'), ('4', '消息页面'), ('3', '发现页面'), ('0', '通用页面'), ('2', '发布页面'), ('1', '活动页面')], default='0', max_length=1, verbose_name='分享页面设置'),
        ),
    ]
