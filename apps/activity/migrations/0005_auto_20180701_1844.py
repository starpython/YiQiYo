# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-01 18:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20180701_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymodel',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='activityimagesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityImagesModel/%y/%d/903abf865aac415783d091d25ab55e15', verbose_name='活动图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/%y/%d/903abf865aac415783d091d25ab55e15', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='groupcode',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/qr/%y/%d/903abf865aac415783d091d25ab55e15', verbose_name='群二维码'),
        ),
        migrations.AlterField(
            model_name='activitytypemodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityTypeModel/%y/%d/903abf865aac415783d091d25ab55e15', verbose_name='类别图片'),
        ),
    ]
