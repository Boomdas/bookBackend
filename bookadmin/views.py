import json
from re import I
import re
from telnetlib import STATUS
from unicodedata import name
from webbrowser import get
from django.shortcuts import render
from .models import BookAdmin
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
from .serializer import BookAdminserializer
import jwt
from datetime import datetime, timedelta
@api_view(['GET'])
def getData(request):
  all_entries = list(BookAdmin.objects.all())
  header = request.headers['user']
  print(header)
  data = []
  for item in all_entries:
    data.append({
      'id':str(item.id),
      'name':item.name
    })
  return HttpResponse(json.dumps(data), content_type='application/json')

@api_view(['GET'])
def getDataById(request):
  id = request.query_params.get('id')
  print(id)
  all_entries = list(BookAdmin.objects.filter(id=id))
  data = []
  for item in all_entries:
    data.append({
      'id':str(item.id),
      'name':item.name
    })
  return HttpResponse(json.dumps(data), content_type='application/json')

@api_view(['POST'])
def adddata(request):
  name = request.data.get('name')
  password = request.data.get('password')
  book = BookAdmin(name = name,password = password)
  # BookAdmin.objects.create(name = name, password = password)
  
  book.save()
  return HttpResponse("ok")

@api_view(['PUT'])
def updatedata(request):
  id = request.query_params.get('id')
  name = request.data.get('name')
  password = request.data.get('password')
  queryset = BookAdmin.objects.filter(id = id).update(name = name, password = password)
  return HttpResponse("ok")

@api_view(['DELETE'])
def deletedata(request):
  id = request.query_params.get('id')
  
  BookAdmin.objects.filter(id=id).delete()
  return HttpResponse("ok")

@api_view(['POST'])
def login(request):
  name = request.data.get('name')
  password = request.data.get('password')
  all_entries = list(BookAdmin.objects.filter(name=name))
  for item in all_entries:
    if item.password == password:
      token = jwt.encode({'employee_id': str(item.id),
                                        'exp': datetime.utcnow() + timedelta(minutes=24)},
                                       "secrate", algorithm="HS256")
      return HttpResponse(json.dumps({'token':token}),status=200)
  return HttpResponse("error",status = 404) 
