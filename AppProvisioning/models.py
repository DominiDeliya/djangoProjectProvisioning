from datetime import datetime
from django.db import models


class Customer(models.Model):
    description = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return 'Customer - {}'.format(self.description)


class Extension(models.Model):
    name = models.CharField(max_length=64)
    extension = models.IntegerField()

    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return 'Ext {}-{}'.format(self.name, self.extension)


class DeviceVendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'Device-Vendor {}'.format(self.name)


class DeviceModel(models.Model):
    class DeviceFormat(models.TextChoices):
        FORMAT_1 = 'FORMAT_1'
        FORMAT_2 = 'FORMAT_2'

    name = models.CharField(max_length=255)
    dss = models.BooleanField(default=False)
    device_format = models.CharField(max_length=45, choices=DeviceFormat.choices, default=DeviceFormat.FORMAT_1)
    vendor = models.OneToOneField(DeviceVendor, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return 'Device-Model {} {}'.format(self.name, self.device_format)


class Device(models.Model):
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=255, unique=True)
    cfg_last_update = models.DateTimeField(default=datetime.now)

    model = models.OneToOneField(DeviceModel, on_delete=models.RESTRICT, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return 'Device {} {}'.format(self.description, self.mac, self.cfg_last_update)


class DSS(models.Model):

    class DssType(models.TextChoices):
        BLF = 'BLF'
        SPD = 'SPD'

    dss_type = models.CharField(max_length=45, choices=DssType.choices, default=DssType.SPD)
    key = models.IntegerField()
    value = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    devices = models.ForeignKey(Device, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return 'DSS {} {} {}'.format(self.dss_type, self.value, self.label)

