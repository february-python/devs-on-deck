from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^devs/dev_register/$', views.dev_register, name='devs'),
]