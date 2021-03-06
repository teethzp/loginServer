"""Mylogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^api/',include('loginapp.urls')),
    url(r'^admin/', admin.site.urls),
]

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import string
import random
from django.conf import settings

sched=BlockingScheduler()

@sched.scheduled_job("cron",second="*/10")
def mytask():
	salt=''.join(random.sample(string.ascii_letters+string.digits,8))
	print salt
	settings.SALT=salt
	print settings.SALT

#sched.start()

def tasktiming():
	salt=''.join(random.sample(string.ascii_letters+string.digits,8))
	print salt
	settings.SALT=salt
	print settings.SALT

scheduler=BackgroundScheduler()
scheduler.add_job(tasktiming,'interval',seconds=100)
scheduler.start()




