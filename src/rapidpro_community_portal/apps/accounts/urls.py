from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.create, name='wagtailusers_users_create'),
    url(r'^([^\/]+)/$', views.edit, name='wagtailusers_users_edit'),
]
