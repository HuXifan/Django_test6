from django.contrib import admin
from django.conf.urls import url, include
from booktest import views
urlpatterns = [
    url(r'^index$', views.index),
]