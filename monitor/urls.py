from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('',views.index,name='index'),
    path('create-device',views.create_device,name='create-device'),
    path('list-devices',views.list_devices_view,name='list-devices'),
    path('display-data/<str:unique_id>/',views.display_plant_data,name='plant-data'),

    # API Endpoints
    path('api/plant-data/',views.receive_plant_data_api),
]