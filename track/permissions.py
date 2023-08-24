from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Company, Employee


class CanCreateCompany(permissions.BasePermission):
    message = "You are not allowed to perform this action, only superuse or staff can perform this action"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSameCompany(permissions.BasePermission):
    message = "You are not allowed to create employees of other companies"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            company_id = request.data.get('company')
            if Company.objects.filter(id=company_id, user=request.user).exists():
                return True
        return False


class IsAssignDevice(permissions.BasePermission):
    message = "You are not allowed to perform this action"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # if request.method == 'POST':
        employee_id = request.data.get('employee')
        employee = get_object_or_404(Employee, id=employee_id)
        if Company.objects.filter(id=employee.company.id, user=request.user).exists():
            return True
        return False


class CanUpdateDeviceLog(permissions.BasePermission):
    message = "You are not allowed to update this device log"

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if Company.objects.filter(id=obj.employee.company.id, user=request.user).exists():
            return True
        return False
