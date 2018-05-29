# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyDetails(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    github = models.CharField(max_length=200)