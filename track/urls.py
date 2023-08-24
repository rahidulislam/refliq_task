from django.urls import path
from .views import CompanyCreateListAPIView, EmployeeCreateListAPIView
app_name = 'track'
urlpatterns = [
    path('company/list-create/', CompanyCreateListAPIView.as_view(),name='company_list_create'),
    path('employee/list-create/', EmployeeCreateListAPIView.as_view(),name='employee_list_create'),
]
