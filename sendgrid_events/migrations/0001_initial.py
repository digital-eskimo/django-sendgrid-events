# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-05 12:29
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=150)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
