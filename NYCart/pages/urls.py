from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add_vendor/', views.addVendor.as_view(), name='add_vendor'),
    path('vendor_grid/', views.vendorList, name="vendor_grid")
]