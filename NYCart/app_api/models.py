from django.db import models
# Create your models here.

class Vendor(models.Model):
    ACTIVE_STATUS =[('Y', 'Active'),
                    ('N', 'Inactive')]

    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)
    active = models.CharField(max_length=1, choices=ACTIVE_STATUS, default='Y')
    email = models.EmailField(max_length=254, blank=True)