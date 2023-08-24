from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .permissions import CanCreateCompany, IsSameCompany
# Create your views here.
class CompanyCreateListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, CanCreateCompany]


class EmployeeCreateListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSameCompany]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)