# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0020_auto_20160324_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='gbaseline',
            name='nada',
            field=models.CharField(blank=True, max_length=34, null=True, verbose_name='nada'),
        ),
    ]
