# myapp/models.py
from django.db import models

class Device(models.Model):
    serial_no = models.CharField(max_length=50)
    device_name = models.CharField(max_length=100)
    ssid = models.CharField(max_length=100)
    rssi = models.IntegerField()
    mac_address = models.CharField(max_length=17)
    status = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.device_name

class Recon(models.Model):
    network = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    detection_date = models.DateField()
    network_id = models.CharField(max_length=100)

    def __str__(self):
        return self.network

class System(models.Model):
    system_status = models.CharField(max_length=20)
    disk_usage = models.IntegerField()
    connected_clients = models.IntegerField()
    ssids_collected = models.IntegerField()
    wireless_encryption = models.IntegerField()
    wireless_landscape = models.IntegerField()

    def __str__(self):
        return self.system_status
