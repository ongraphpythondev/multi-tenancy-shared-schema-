from dataclasses import field
from rest_framework import serializers
from tenant.models import TenantSerializers
from .models import Company, Department, Branch, Employee,Client
from tenant.utils import tenant_from_request
class CompanySerializer(TenantSerializers):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(TenantSerializers):
    class Meta:
        model = Department
        fields = '__all__'
    
class BranchSerializer(TenantSerializers):

    class Meta:
        model = Branch
        fields = '__all__'


class EmployeeSerializer(TenantSerializers):
    class Meta:
        model = Employee
        fields = '__all__'

class ClientSerializer(TenantSerializers):
    class Meta:
        model = Client
        fields = '__all__'




