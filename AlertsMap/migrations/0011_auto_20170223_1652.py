# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-23 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlertsMap', '0010_auto_20170223_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries_adult',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries_children',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries_elderly',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries_females',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='gap_beneficiaries_males',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='response_partner',
        ),
    ]