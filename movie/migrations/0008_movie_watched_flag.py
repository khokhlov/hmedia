# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-28 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20170331_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watched_flag',
            field=models.BooleanField(default=False, verbose_name='Watched'),
        ),
    ]
