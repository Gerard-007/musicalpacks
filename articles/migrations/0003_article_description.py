# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-16 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180914_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
