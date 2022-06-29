# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-22 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0018_headers_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headers',
            name='button',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='headers',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
