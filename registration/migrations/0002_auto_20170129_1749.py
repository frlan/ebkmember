# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='fee',
            field=models.FloatField(choices=[('normal', '24'), ('reduced', '18'), ('other', '0')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='memberstatus',
            field=models.CharField(choices=[('member', 'Mitglied'), ('sustaining_member', 'Fördermitglied')], max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], max_length=25),
        ),
    ]
