# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0063_auto_20160420_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='gbaseline',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Starting date'),
        ),
    ]
