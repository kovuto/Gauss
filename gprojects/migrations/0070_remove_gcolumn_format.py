# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0069_auto_20160429_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gcolumn',
            name='format',
        ),
    ]
