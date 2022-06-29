from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=64)
    state = serializers.CharField(max_length=64)
    zip_code = serializers.CharField(max_length=5)
    active = serializers.CharField(max_length=1)
    email = serializers.EmailField(max_length=254, allow_blank=True)

    class Meta:
        model = Vendor
        fields = ('__all__')