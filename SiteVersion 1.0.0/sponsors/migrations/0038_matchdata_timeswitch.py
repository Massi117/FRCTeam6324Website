# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0037_auto_20180224_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='timeSwitch',
            field=models.FloatField(default=0),
        ),
    ]
