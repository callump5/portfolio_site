# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.TextField(default='f'),
            preserve_default=False,
        ),
    ]