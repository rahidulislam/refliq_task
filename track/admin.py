from django.contrib import admin
from .models import Company, Employee
# Register your models here.
admin.site.register(Company)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['company', 'job_title', 'department', 'user']