# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0058_auto_20160420_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcolumn',
            name='content',
            field=models.CharField(choices=[('estimate_time_days', 'Duration'), ('early_start', 'Early start'), ('last_finish', 'Last Finish')], default='estimate_time_days', max_length=30, verbose_name='Content of the column'),
        ),
    ]
