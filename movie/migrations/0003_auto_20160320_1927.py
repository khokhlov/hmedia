# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160320_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Year'),
        ),
    ]
