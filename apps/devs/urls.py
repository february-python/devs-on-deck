from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^success/$', views.success, name="success"),
    url(r'register/$', views.register, name='register'),
    url(r'create_dev/$', views.create_dev, name='create_dev'),
    url(r'^languages/$', views.languages, name="languages"),
    url(r'^addlanguages/$', views.addlanguages, name="addlanguages"),
    url(r'^frameworks/$', views.frameworks, name="frameworks"),
    url(r'^addframeworks/$', views.addframeworks, name="addframeworks"),
    url(r'login_dev/$', views.login_dev, name='login_dev'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^messages/$', views.messages, name="messages"),
]
