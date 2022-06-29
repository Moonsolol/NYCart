from django import forms
from django.apps import apps

Vendor = apps.get_model('app_api', 'Vendor')

class NewVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
        labels = {'zip_code': 'Zip Code'}