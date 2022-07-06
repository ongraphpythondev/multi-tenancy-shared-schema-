from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('company/', CompanyViewSet.as_view()),
    path('branch/', BranchViewSet.as_view()),
    path('department/', DepartmentViewSet.as_view()),
    path('employee/', EmployeeViewSet.as_view()),
    path('client/', ClientViewSet.as_view()),

]