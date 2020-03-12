# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 16:18
# @Author  : Jackey-lu
# @File    : urls.py

from django.contrib import admin
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path('/news/story', views.introduce),
    path('login', views.login),
    path('home', views.home),
]