"""Alisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #for /study
    #url(r'^$',views.login,name='login'),
    url(r'^auth/$',views.auth_view,name='auth_view'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^auth/loggedin/$',views.loggedin,name='loggedin'),
    url(r'^auth/invalid/$',views.invalid_login,name='invalid_login'),
    #for /study/12345678 any digit
    #url(r'^(?P<Research_ID>[0-9]+)/$',views.ResearchDetails,name='ResearchDetails'),
   
]
