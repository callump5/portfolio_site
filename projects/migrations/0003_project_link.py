# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180525_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.TextField(default='wr'),
            preserve_default=False,
        ),
    ]