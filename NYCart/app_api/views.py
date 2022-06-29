from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import VendorSerializer
from .models import Vendor
# Create your views here.

class VendorView(APIView):
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            vendor = Vendor.objects.get(id=id)
            serializer = VendorSerializer(vendor)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        vendor = Vendor.objects.get(id=id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        vendor = get_object_or_404(Vendor, id=id)
        vendor.delete()
        return Response({"status": "success", "data": "Item Deleted"})