# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-22 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AlertsMap', '0002_auto_20170222_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='AlertsMap.Album')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterField(
            model_name='response',
            name='alert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dwarves', to='AlertsMap.Alert'),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('album', 'order')]),
        ),
    ]