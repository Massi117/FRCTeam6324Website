# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-17 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsormodel',
            name='sponsorclass',
        ),
        migrations.AddField(
            model_name='sponsormodel',
            name='slug',
            field=models.CharField(db_index=True, default='hello', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
