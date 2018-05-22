from django.conf.urls import url

from views import get_about

urlpatterns = [
    url(r'^about/$', get_about),
]