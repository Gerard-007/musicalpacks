# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-28 11:27
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180928_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_dir),
        ),
    ]
