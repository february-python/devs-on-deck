from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^success/$', views.success, name="success"),
    url(r'^devreg/$', views.devreg, name="devreg"),
    url(r'^languages/$', views.languages, name="languages"),
]
