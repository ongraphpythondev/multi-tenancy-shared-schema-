from dataclasses import fields
from django.db import models
from rest_framework import serializers
# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100,unique=True)


# Model used to separate data for each domain   
class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class TenantSerializers(serializers.ModelSerializer):
   class Meta:
    model = Tenant
    fields = ['name']