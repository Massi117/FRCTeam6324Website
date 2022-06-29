# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-14 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0008_homemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='membermodel',
            old_name='name',
            new_name='student',
        ),
    ]