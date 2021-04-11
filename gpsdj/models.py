from django.db import models
# from django_google_maps import fields as map_fields

class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    company_token = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Devices(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=50, unique=True)
    device_model = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    app = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    # address = map_fields.AddressField(max_length=200)
    latitude = models.IntegerField(default=0) #map_fields.GeoLocationField(max_length=100)
    longitude = models.IntegerField(default=0) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    device_id = models.CharField(max_length=50, unique=True)
    data = models.JSONField(null=True)
    
    def __str__(self):
        return self.name