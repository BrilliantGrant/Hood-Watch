# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watch.Neighborhood'),
        ),
    ]
