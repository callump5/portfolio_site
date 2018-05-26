# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='brief',
            field=models.CharField(default='k', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
