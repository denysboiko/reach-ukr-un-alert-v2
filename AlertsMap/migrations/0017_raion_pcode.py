# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-14 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlertsMap', '0016_auto_20170309_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='raion',
            name='pcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]