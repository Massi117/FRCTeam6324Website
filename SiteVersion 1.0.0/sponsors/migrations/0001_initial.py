# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-17 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('sponsorclass', models.CharField(db_index=True, max_length=10)),
            ],
        ),
    ]
