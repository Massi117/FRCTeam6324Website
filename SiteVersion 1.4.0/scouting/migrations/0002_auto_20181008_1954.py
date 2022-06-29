# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scouting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoutdata',
            name='event',
        ),
        migrations.AddField(
            model_name='matchdata',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='scouting.EventModel'),
            preserve_default=False,
        ),
    ]
