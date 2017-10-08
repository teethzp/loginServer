# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Userinfo
from .serializers import UserinfoSerializer
import time
import hashlib
from django.conf import settings
# Create your views here.

@api_view(['GET','PUT'])
def Userinfo_detail(request,pk):
	try:
		userinfo=Userinfo.objects.get(pk=pk)
	except Userinfo.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method=='GET':
#		serializer=UserinfoSerializer(userinfo)
#		return Response(serializer.data)
		return Response(settings.SALT)

	if request.method=='PUT':
		serializer=UserinfoSerializer(data=request.data)
		print(serializer)
		##verify the data from browser weather efficacious!
		if serializer.is_valid():
			#name=serializer['username'] -- wrong
			name=serializer.data['username']
			passwd=serializer.data['password']
			timestamp=serializer.data['timestamp']
			print(serializer.data)
			##verify timestamp!
			tp_client=float(serializer.data['timestamp'])
			tp_local=time.time()
			if((tp_local-tp_client)>500):
				return Response(status=status.HTTP_400_BAD_REQUEST)
			##verify timestamp successed!
			##According username from browers get corresponding userinfo from database
			try:##Do not forget judge weather able to get the userinfo from database!
				userinfo_db=Userinfo.objects.get(username=name)
				serializer_db=UserinfoSerializer(userinfo_db)
			except Userinfo.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
			##Get MD5 passwd_db from database 
			passwd_db=serializer_db.data['password']
			##MD5 passwd_db+timestamp
			md5_=hashlib.md5() #create a md5 instance
			md5_.update(passwd_db+timestamp) #generate the encrypted string
			pw_server=md5_.hexdigest() #get the encrypted string
			##verify password with timestamp
			if pw_server==passwd:
				return Response(status=status.HTTP_200_OK)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			#if Userinfo.objects.filter(username=name,password=passwd):
			#	return Response(status=status.HTTP_201_CREATED)
			#else:	
			#	return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)














