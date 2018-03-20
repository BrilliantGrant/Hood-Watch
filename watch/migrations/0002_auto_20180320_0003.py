# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hood',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='watch.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(max_length=160),
        ),
    ]