# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project (models.Model):
    thumb = models.ImageField(upload_to="images", blank=True, null=True)
    link = models.CharField(max_length=200)
    git = models.CharField(max_length=200)

    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)

    description = models.TextField()

    def __unicode__(self):
        return str(self.id) + ' - ' + self.title

class ProjectGoal (models.Model):
    job = models.ForeignKey(Project, related_name='Goal')

    goal = models.CharField(max_length=100)


    def __unicode__(self):
        return self.job.title + ' - ' + self.goal