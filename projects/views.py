# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from models import *

def get_projects(request):

    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})

def get_project_details(request, id):

    project = get_object_or_404(Project, pk=id)
    goals = ProjectGoal.objects.filter(job=id)

    return render(request, 'projects/project.html', {'project': project,
                                                     'goals': goals})