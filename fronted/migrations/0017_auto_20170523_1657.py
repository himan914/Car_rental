# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fronted', '0016_auto_20170523_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='car',
        ),
        migrations.AddField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fronted.Product'),
        ),
    ]
