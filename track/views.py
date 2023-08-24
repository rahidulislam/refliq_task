from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .permissions import CanCreateCompany, IsSameCompany, IsAssignDevice,CanUpdateDeviceLog 

# Create your views here.
class CompanyCreateListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, CanCreateCompany]

    def perform_create(self, serializer):
        
        return serializer.save(user=self.request.user)


class EmployeeCreateListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSameCompany]

class DeviceCreateListAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsSameCompany]

class DeviceDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsSameCompany]
    http_method_names = ['get', 'patch', 'delete']

class DeviceLogCreateListAPIView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssignDevice]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if DeviceLog.objects.filter(device=serializer.validated_data['device'], employee=serializer.validated_data['employee']).exists():
            return Response({"detail":"Device already checked out"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeviceLogDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated, CanUpdateDeviceLog]
    http_method_names = ['get', 'patch', 'delete']