# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 09:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0046_gcolumn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcolumn',
            name='pos',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)], verbose_name='Horizontal position'),
        ),
    ]
