from django.urls import path
from . import views

urlpatterns = [
  path('getauthor/',views.getauthor),
  path('getaddauthor/',views.getauthorbyid),
  path('addauthor/',views.addauthor),
]