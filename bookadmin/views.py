from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
  person = {'name':'hiii', 'son-name':'rohit'}
  return Response(person)