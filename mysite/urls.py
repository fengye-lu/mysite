"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cur_time', views.cur_time),
    path('userInfo', views.userInfo),
    re_path(r'^articles/[0-9]{4}/$', views.year_archive),
    # re_path(r'^article/([0-9]{4})/([0-9]{2})/$', views.year_archives),
    re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_archives),
    # 按照命名去拿值
    path('index', views.index, name='lzh'),

    path('blog/', include('blog.urls')),  # 分发路径
]
