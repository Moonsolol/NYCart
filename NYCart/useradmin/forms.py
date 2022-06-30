from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'First name', 'last_name': 'Last Name', 'email': 'Email'}