# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouting', '0002_auto_20181008_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='script',
            field=models.CharField(db_index=True, default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
