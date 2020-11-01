from django.urls import path
from app_DataSelect import views

urlpatterns = [
    path('',views.select),


]