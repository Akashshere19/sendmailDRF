from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
  path('send',views.send_email,name='sendmail'),
  path('get_event_details/',EmployeeEventDetails.as_view(), name='get_event_details'),
]
