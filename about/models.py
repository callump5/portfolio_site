# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Qualification(models.Model):
    qualification = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.qualification


class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.skill

class Frameworks(models.Model):
    framework = models.CharField(max_length=100)

    def __unicode__(self):
        return self.framework