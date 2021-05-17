from rest_framework import serializers
from .models import Device, Customer, Extension, DeviceVendor, DeviceModel, DSS


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension
        fields = '__all__'


class DeviceVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceVendor
        fields = '__all__'


class DeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'


class DSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSS
        fields = '__all__'
