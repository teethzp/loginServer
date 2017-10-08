# -*- coding:utf-8 -*-
from django.conf.urls import url
import views

urlpatterns=[
	url(r'userinfos/(?P<pk>[0-9]+)$',views.Userinfo_detail,name='Userinfo_detail'),
]
