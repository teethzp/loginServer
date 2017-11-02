#!/usr/bin/env python
#coding:utf-8
import os
import django

import hashlib

#import sys
#reload(sys)
#sys.setdefaultencoding('gbk')

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Mylogin.settings")
django.setup()

def main():
	from loginapp.models import Userinfo
	f=open("userdata.txt")
	md5_=hashlib.md5()
	md5_.update('123')
	psswd=md5_.hexdigest()
	for line in f:
		#md5_=hashlib.md5()
		name,pwd=line.split(',')
		#print(pwd)
		#md5_.update(pwd)
		#pwd=md5_.hexdigest()
		Userinfo.objects.create(username=name,password=psswd,timestamp="0")
		print(name+' '+psswd)
	f.close()

if __name__=="__main__":
	main()
	print("Completed!")

