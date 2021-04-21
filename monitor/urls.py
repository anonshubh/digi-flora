from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('',views.index,name='index'),
    path('create-device',views.create_device,name='create-device'),
    path('list-devices',views.list_devices_view,name='list-devices'),
]