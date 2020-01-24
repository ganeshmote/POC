from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('login/', user_login,name='user_login'),
    path('logout/', user_logout,name='user_logout'),
    path('dashboard/', dashboard,name='dashboard'),
    path('rssdata_view/', rssdata_view,name='rssdata_viev'),
    path('classified_view/', Rssfeedclassified_view,name='Rssfeedclassified_view'),
    path('rssdatadel_view/', rssdatadel_view,name='rssdatadel_view'),
    path('classifieddel_view/', Rssfeedclassifiedsel_view,name='classifieddel_view'),
    path('insertDB/', insertDB,name='insertDB'),
]

