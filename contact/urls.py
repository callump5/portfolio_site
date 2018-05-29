from django.conf.urls import url

from .views import contact_info

urlpatterns = [
    url(r'^contact/$', contact_info),
]