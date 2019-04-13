# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-22 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180921_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='by',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]