# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20170215_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='entrydate',
            field=models.DateField(null=True),
        ),
    ]
