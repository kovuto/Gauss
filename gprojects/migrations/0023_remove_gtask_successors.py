# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0022_remove_gbaseline_nada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gtask',
            name='successors',
        ),
    ]
