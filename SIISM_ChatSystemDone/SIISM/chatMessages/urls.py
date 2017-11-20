from django.conf.urls import patterns, url

from . import views

urpatterns = patterns('',
    url(r'^$', views.chat, name ='chat'),
)