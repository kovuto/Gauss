# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0010_gproject_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gbaseline',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Is it the active one?'),
        ),
    ]
