# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0030_auto_20180222_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoutdata',
            name='script',
        ),
    ]
