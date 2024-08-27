from django.shortcuts import render , redirect
from rest_framework import viewsets
from .models import Device, Order
from .serializers import DeviceSerializer, OrderSerializer

from .forms import DeviceForm

def home(request):
    devices = Device.objects.all()
    return render(request, 'home.html', {'devices': devices})

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeviceForm()

    return render(request, 'add_device.html', {'form': form})


