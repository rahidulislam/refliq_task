from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog
# Register your models here.
admin.site.register(Company)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['company', 'job_title', 'department', 'user']
    list_filter = ['company', 'job_title', 'department']


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'model', 'assigned_to', 'status', ]
    list_filter = ['asset_type', 'model', 'assigned_to',]


@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['device', 'employee', 'check_out_date', ]
    list_filter = ['device', 'employee', 'check_out_date',]
