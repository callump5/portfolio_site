# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.



def upload_project_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class Project (models.Model):
    thumb = models.ImageField(upload_to=upload_project_img, blank=True, null=True)
    link = models.CharField(max_length=200)
    git = models.CharField(max_length=200)

    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)

    description = HTMLField()

    def __unicode__(self):
        return str(self.id) + ' - ' + self.title

class ProjectGoal (models.Model):
    job = models.ForeignKey(Project, related_name='Goal')

    goal = models.CharField(max_length=100)


    def __unicode__(self):
        return self.job.title + ' - ' + self.goal