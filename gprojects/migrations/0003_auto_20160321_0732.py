# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0002_gproject_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gproject',
            options={'ordering': ['active', 'created']},
        ),
    ]
