from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'', views.home_page, name='home_page'),
]
