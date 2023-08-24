from django.urls import path
from .views import CompanyCreateListAPIView, EmployeeCreateListAPIView, DeviceCreateListAPIView,DeviceLogCreateListAPIView, DeviceDetailUpdateDeleteAPIView,DeviceLogDetailUpdateDeleteAPIView
app_name = 'track'
urlpatterns = [
    path('company/list-create/', CompanyCreateListAPIView.as_view(),name='company_list_create'),
    path('employee/list-create/', EmployeeCreateListAPIView.as_view(),name='employee_list_create'),
    path('device/list-create/', DeviceCreateListAPIView.as_view(),name='device_list_create'),
    path('device/retr-up-del/<int:pk>/',DeviceDetailUpdateDeleteAPIView.as_view(),name='device_retrieve_update_delete'),
    path('log/list-create/',DeviceLogCreateListAPIView.as_view(),name='log_list_create'),
    path('log/retr-up-del/<int:pk>/',DeviceLogDetailUpdateDeleteAPIView.as_view(),name='log_retrieve_update_delete'),

]
