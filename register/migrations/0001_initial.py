# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membertype', models.CharField(choices=[('normal', 'ordentliche Mitgliedschaft'), ('foerder', 'Fördermitgliedschaft'), ('firma', 'Firmenmitgliedschaft')], default='normal', max_length=10)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=10)),
                ('country', django_countries.fields.CountryField(default='DE', max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateTimeField(blank=True)),
                ('entrydate', models.DateTimeField(blank=True)),
                ('submitted_dt', models.DateTimeField(blank=True)),
                ('fee', models.CharField(choices=[('normal;24', 'Normal – 24€ / Monat'), ('discount;18', 'Ermäßigt – 18€ / Monat'), ('junior;8', 'Junior – 8€ / Monat'), ('company;100', 'Firma/Institution – 100€ / Monat'), ('custom', 'anderer')], default='normal', max_length=100)),
                ('customfee', models.PositiveIntegerField()),
                ('iban', localflavor.generic.models.IBANField(include_countries=('AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'GB', 'GI', 'GR', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'SM'), max_length=34, use_nordea_extensions=False)),
                ('sepa_agree', models.BooleanField()),
            ],
        ),
    ]