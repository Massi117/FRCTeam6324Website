# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-21 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(blank=True),
        ),
    ]