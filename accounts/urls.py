from django.conf.urls import url

from . import views
from . import forms

urlpatterns = [
    url(r'^new/$', views.create, name='wagtailusers_users_create'),
    url(r'^([^\/]+)/$', views.edit, name='wagtailusers_users_edit'),
]
