# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

###

# Create your models here.

class Userinfo(models.Model):
	username=models.CharField(max_length=300)
	password=models.CharField(max_length=300)
	timestamp=models.CharField(max_length=20)
