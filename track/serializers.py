from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name', 'description',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','user','company', 'job_title', 'department', )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','company', 'assigned_to', 'status', 'asset_type', 'model', 'serial_number', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['log'] = DeviceLogSerializer(instance.devicelog_set.all(), many=True).data
        return rep

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
