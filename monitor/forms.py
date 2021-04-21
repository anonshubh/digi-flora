from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):
    """
    Form to Store Data in Device Model
    """
    class Meta:
        model = Device
        exclude = ('user','unique_id','plant','active')