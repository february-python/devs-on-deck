from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^org_register/$', views.org_register, name='org_reg'),
    url(r'^register/', views.org_register_page, name='reg_page'),
    url(r'^org_login/', views.org_login, name='org_login'),
    url(r'^org_logoff/', views.org_logoff, name='org_logoff'),
    url(r'^login/', views.org_login_page, name='org_page')
]