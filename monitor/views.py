from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.core.exceptions import ValidationError,PermissionDenied
from django.contrib import messages

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

