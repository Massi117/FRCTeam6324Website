# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0027_auto_20180220_0325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scoutdata',
            old_name='slug',
            new_name='script',
        ),
    ]
