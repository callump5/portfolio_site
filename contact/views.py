# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *
# Create your views here

def contact_info(request):
    details = MyDetails.objects.all
    return render(request, 'contact/contact.html', {'details': details})