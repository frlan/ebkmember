# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20170204_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sepa_agree',
            field=models.NullBooleanField(),
        ),
    ]
