# myapp/views.py
from rest_framework import generics
from .models import Device, Recon, System
from .serializers import DeviceSerializer, ReconSerializer, SystemSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ReconListCreateView(generics.ListCreateAPIView):
    queryset = Recon.objects.all()
    serializer_class = ReconSerializer

class ReconRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recon.objects.all()
    serializer_class = ReconSerializer

class SystemListCreateView(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

class SystemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
