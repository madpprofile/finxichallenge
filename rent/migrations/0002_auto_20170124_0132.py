# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='apartment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]