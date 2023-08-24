from rest_framework import permissions
from .models import Company

class CanCreateCompany(permissions.BasePermission):
    message = "You are not allowed to create companies"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user.is_staff

class IsSameCompany(permissions.BasePermission):
    message = "You are not allowed to create employees of other companies"
    
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.method == 'POST':
            company_id= request.data.get('company')
            if company_id and hasattr(request.user, 'employee'):
                company= Company.objects.get(id=company_id)
                return company == request.user.employee.company
        return True