"""hostelManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name = 'homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminpage', views.adminpage, name='adminpage'),

    path('userlogin',views.userlogin,name='userlogin'),
    path('userpage',views.userpage,name='userpage'),

    path('showdata', views.showdata, name='showdata'),
    path('insertdata', views.insertdata, name='insertdata'),
    path('updatedata', views.updatedata, name='updatedata'),
    path('deletedata', views.deletedata, name='deletedata'),

    path('showstat', views.showstat, name='showstat'),
    path('prefresult',views.prefresult,name='prefresult'),

    path('reviewpage',views.reviewpage,name='reviewpage'),
    path('insertreview',views.insertreview,name='insertreview'),
    path('searchreview',views.searchreview,name='searchreview'),
]
urlpatterns += staticfiles_urlpatterns()
