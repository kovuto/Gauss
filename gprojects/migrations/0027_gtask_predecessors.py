# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0026_remove_gtask_predecessors'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtask',
            name='predecessors',
            field=models.ManyToManyField(blank=True, related_name='successors', to='gprojects.Gtask'),
        ),
    ]
