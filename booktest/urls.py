from django.contrib import admin
from django.conf.urls import url, include
from booktest import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^editor$', views.editor),
    url(r'^show/$', views.show),
]
