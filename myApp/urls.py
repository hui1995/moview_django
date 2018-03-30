
from django.conf.urls import url, include
from django.contrib import admin

from myApp import views

urlpatterns = [

    url(r'^test/$',views.test),
    url(r'^index/',views.index),
    url(r'^like/$',views.like,name='like'),
    url(r'^login/',views.login,name='login'),
    url(r'^signup/$',views.signup,name='signup')


        ]