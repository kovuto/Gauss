# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0017_auto_20160323_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtask',
            name='percentage_complete',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Percentage complete'),
        ),
    ]
