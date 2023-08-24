from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='%(class)s_owner')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='%(class)s_employee')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title= models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username

class Device(models.Model):
    DEVICE_STATUS_CHOICES = [
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, default='available')
    asset_type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    
    

    def __str__(self):
        return f"{self.asset_type} - {self.serial_number}"

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition_at_check_out = models.TextField()
    condition_at_check_in = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.check_out_date}"
