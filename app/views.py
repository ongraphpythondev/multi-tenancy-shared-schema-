
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from tenant.utils import tenant_from_request
# Create your views here.
from .models import Company, Employee, Branch, Department, Client
from .serializers import CompanySerializer, DepartmentSerializer,EmployeeSerializer,BranchSerializer,ClientSerializer
import json
from tenant.models import Tenant
from rest_framework import status
class CompanyViewSet(ListCreateAPIView):
    queryset = Company.objects.all()
    # print(queryset)
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        print(tenant)
        return super().get_queryset().filter(tenant=tenant)
    def post(self, request, *args,**kwargs):
        tenant_form = Tenant.objects.filter(id=request.POST.get('tenant')).first()
        tenant_db = tenant_from_request(self.request)
        print(tenant_form,tenant_db)
        if tenant_form != tenant_db:
            return Response({'msg':'You have no permission!'})
        return super().post(request,*args,**kwargs)
# branch  
class BranchViewSet(ListCreateAPIView):
    queryset = Branch.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    serializer_class = BranchSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    def post(self, request, *args,**kwargs):
        tenant_form = Tenant.objects.filter(id=request.POST.get('tenant')).first()
        tenant_db = tenant_from_request(self.request)
        print(tenant_form,tenant_db)
        if tenant_form != tenant_db:
            return Response({'msg':'You have no permission!'})
        print(request.POST.get('company'))
        company = Company.objects.filter(id=request.POST.get('company'),tenant=request.POST.get('tenant'))
        print(company)
        if not company:
            return Response({'msg':'select right company'})
        return super().post(request,*args,**kwargs)
# department  
class DepartmentViewSet(ListCreateAPIView):
    queryset = Department.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    def create(self, request, *args,**kwargs):
        tenant_form = Tenant.objects.filter(id=request.POST.get('tenant')).first()
        tenant_db = tenant_from_request(self.request)
        print(tenant_form,tenant_db)
        if tenant_form != tenant_db:
            return Response({'msg':'You have no permission!'})
        return super().post(request,*args,**kwargs)
# employee   
class EmployeeViewSet(ListCreateAPIView):
    queryset = Employee.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    def create(self, request, *args,**kwargs):
        tenant_form = Tenant.objects.filter(id=request.POST.get('tenant')).first()
        tenant_db = tenant_from_request(self.request)
        print(tenant_form,tenant_db)
        if tenant_form != tenant_db:
            return Response({'msg':'You have no permission!'})
        return super().post(request,*args,**kwargs)
# client   
class ClientViewSet(ListCreateAPIView):
    queryset = Client.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    def create(self, request, *args,**kwargs):
        tenant_form = Tenant.objects.filter(id=request.POST.get('tenant')).first()
        tenant_db = tenant_from_request(self.request)
        print(tenant_form,tenant_db)
        if tenant_form != tenant_db:
            return Response({'msg':'You have no permission!'})
        return super().post(request,*args,**kwargs)
