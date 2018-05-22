# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *

# Create your views here.


def get_about(request):
    skills = Skill.objects.all()
    frameworks = Frameworks.objects.all()
    qualification = Qualification.objects.all()
    return render(request, 'about/about.html', {'skills': skills,
                                                'frameworks': frameworks,
                                                'qualification': qualification})