from distutils.command.upload import upload
from itertools import tee
from django.db import models
from tenant.models import TenantAwareModel
# Create your models here.


class Company(TenantAwareModel):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,unique=True,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    province = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    postal_code = models.IntegerField()
    company_logo = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=250)
    website = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s"%(self.name,self.phone_number)

class Branch(TenantAwareModel):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    name =models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    address = models.CharField(max_length=250)

    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class Department(TenantAwareModel):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(TenantAwareModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=150, null=True, blank=True)
    
    profile_image = models.ImageField(max_length=200, upload_to='profile_images/')  
        
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
       
    def __str__(self):
        return "%s %s" % (self.name, self.branch)
    
class Client(TenantAwareModel):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=50)
    profile_image = models.ImageField(max_length=200, upload_to='profile_images/')  
    join_date = models.DateField(auto_now_add=True)
    
    employees = models.ForeignKey(Employee, on_delete=models.PROTECT)
    
    def __str__(self):
        return "%s %s" % (self.name, self.employee)