# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-09 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20180709_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/e5b3982e8dd741ed820c340eb0a6a1a8'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/e5b3982e8dd741ed820c340eb0a6a1a8', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='604300a74219446e95833f8f35cf005c', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
