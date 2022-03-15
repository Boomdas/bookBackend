from django.urls import path
from . import views

urlpatterns = [
  path('', views.getData),
  path('addData',views.adddata),
  path('getdatabyid/',views.getDataById),
  path('updateData',views.updatedata),
  path('deleteData',views.deletedata),
  path('login',views.login)
]