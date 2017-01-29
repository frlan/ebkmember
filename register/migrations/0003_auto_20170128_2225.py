# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20170128_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberregistration',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='memberregistration',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='DE', max_length=2),
        ),
        migrations.AlterField(
            model_name='memberregistration',
            name='customfee',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]