from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('dashboard/logout/', user_logout, name='user_logout'),
    path('dashboard/feeds_list/logout/', user_logout, name='user_logout_dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/processRSS/', processRSS, name='RSS'),
    path('classify/', classifier, name='RSSclassifier'),
    path('RSS/', classifyRSS, name='classifyRSS'),
    path('dashboard/feeds_list/',index,name = 'get_data'),
    path('dashboard/feeds_list/<int:id>/rss_details/',rss_details,name = 'rss_details'),
    path('Insert_data/',insertDB,name = 'insert_data'),
    path('<int:id>/rss_edit/',Rss_feed_edit,name = 'rss_edit'),
    path('back_to_feed/',back_to_feedlist,name = 'back_to_feed'),
    #############################################################
    path('rss_json/',json_response,name = 'rss_json'),
    path('dashboard1/',dashboard1,name = 'dashboard1')
]