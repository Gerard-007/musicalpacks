# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-26 12:38
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_follow_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='../img/icons/musicadence.jpg', upload_to=accounts.models.upload_dir),
        ),
    ]
