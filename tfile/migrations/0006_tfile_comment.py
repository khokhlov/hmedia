# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfile', '0005_auto_20160325_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='tfile',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]
