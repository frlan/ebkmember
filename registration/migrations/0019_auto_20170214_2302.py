# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20170214_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='bankname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='bic',
        ),
        migrations.RemoveField(
            model_name='member',
            name='sex',
        ),
    ]
