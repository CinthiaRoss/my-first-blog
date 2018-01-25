# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:48:49 2018

@author: kreamas
"""

from django.conf.urls import url
from.import views

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'), 
    url(r'^post/(?P>pk\d+)/$', views.post_detail, name = 'post_detail'),           
]