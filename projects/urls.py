from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^projects/$', get_projects),
    url(r'^projects/project-(?P<id>\d)/$', get_project_details)
]