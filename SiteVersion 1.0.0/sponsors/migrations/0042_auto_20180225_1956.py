# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-25 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0041_auto_20180225_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scoutdata',
            old_name='autoSxcale',
            new_name='autoScale',
        ),
    ]
