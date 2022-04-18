import json
from re import I
import re
from telnetlib import STATUS
from unicodedata import name
from webbrowser import get
from django.shortcuts import render
from .models import author
from rest_framework.decorators import api_view
# from django.core import serializers
from django.http import HttpResponse
# from .serializer import BookAdminserializer
import jwt
# from datetime import datetime, timedelta

@api_view(['GET'])
def getauthor(request):
  all_entries = list(author.objects.all())
  # header = request.headers['user']
  # print(header)
  data = []
  for item in all_entries:
    data.append({
      'id':str(item.id),
      'name':item.name,
      'image':item.image,
      'description':item.description,
    })
  return HttpResponse(json.dumps(data), content_type='application/json')

@api_view(['GET'])
def getauthorbyid(request):
  id = request.query_params.get('id')
  print(id)
  all_entries = list(author.objects.filter(id=id))
  data = []
  for item in all_entries:
    data.append({
      'id':str(item.id),
      'name':item.name,
      'image':item.image,
      'description':item.description,
    })
  return HttpResponse(json.dumps(data), content_type='application/json')

@api_view(['POST'])
def addauthor(request):
  name = request.data.get('name')
  image=request.data.get('image')
  description=request.data.get('description')
  author1 = author(name = name,image=image,description = description)  
  author1.save()
  return HttpResponse("author added")


