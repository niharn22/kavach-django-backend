# myapp/serializers.py
from rest_framework import serializers
from .models import Device, Recon, System

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class ReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recon
        fields = '__all__'

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'
