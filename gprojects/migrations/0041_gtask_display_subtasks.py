# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0040_gbaseline_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtask',
            name='display_subtasks',
            field=models.CharField(choices=[('none', 'none'), ('block', 'block')], default='none', max_length=7, verbose_name='Display subtasks'),
        ),
    ]
