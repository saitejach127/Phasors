# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-16 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ismentor',
            field=models.BooleanField(default=False),
        ),
    ]
