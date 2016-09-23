from django.conf.urls import url

from . import views

app_name='senti'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.index, name='index'),

]
