# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-22 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlertsMap', '0004_auto_20170222_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='response_partners',
        ),
    ]