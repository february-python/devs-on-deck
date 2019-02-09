from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'create_dev/$', views.create_dev, name='create_dev'),
    url(r'login/$', views.login, name='login'),
    url(r'login_dev/$', views.login_dev, name='login_dev'),
    url(r'dashboard/$', views.dashboard, name='dashboard')
]