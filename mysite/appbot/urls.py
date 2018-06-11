from django.urls import path

from . import views

app_name = 'appbot'
urlpatterns = [
    path('', views.appb, name='appb'),


]
  
