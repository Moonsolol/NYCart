from django.urls import path
from .views import VendorView

urlpatterns = [
    path('vendors/', VendorView.as_view()),
    path('vendors/<int:id>', VendorView.as_view())
]