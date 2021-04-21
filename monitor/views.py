from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.core.exceptions import ValidationError,PermissionDenied
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Plant,Device
from .forms import DeviceForm


# Renders the Index Page
def index(request):
    return render(request,'monitor/index.html')


# Creates a New Device
@login_required
def create_device(request):
    form = DeviceForm()
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            current_device_count = Device.objects.all().count()
            current_device_count+=1
            device_id = f"SRD0{current_device_count}"

            instance.user = request.user
            instance.unique_id = device_id
            instance.save()

            device_obj = get_object_or_404(Device,unique_id=device_id)
            messages.info(request,f"New Device Successfully Created!")
            return render(request,'monitor/create-success.html',{'device_obj':device_obj})
        else:
            messages.error(request,"Form is Invalid! ,Kindly Re-Submit")
    return render(request,'monitor/create-device.html',{'form':form})


# Returns the List of Available Devices of Particular User
@login_required
def list_devices_view(request):
    devices = Device.objects.filter(user=request.user,active=True)
    return render(request,'monitor/list-devices.html',{'devices':devices})


# Receives the Data from Sensor and Stores in db
@csrf_exempt
def receive_plant_data_api(request):
    if request.method == "POST":
        data =  json.loads(request.body)
        device_id = data.get('device_id')
        device_obj = get_object_or_404(Device,unique_id=device_id)

        plant_obj = Plant.objects.create(
            name = data.get('name'),
            moisture = int(data.get('moisture')),
            temperature = int(data.get('temperature')),
            humidity = int(data.get('humidity')),
            light = int(data.get('light'))
        )

        device_obj.plant.add(plant_obj)
        return JsonResponse({"Success":"Plant Data Successfully Received!"},status=200)

    return HttpResponseNotAllowed()
