from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Plant(models.Model):
    """
    Stores the Data Received from Sensor
    """
    name = models.CharField(max_length=128)
    moisture = models.PositiveIntegerField()
    temperature = models.PositiveIntegerField()
    humidity = models.PositiveIntegerField()
    light = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return (self.name)[:15]


class Device(models.Model):
    """
    Stores the Information About Device
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    device_name = models.CharField(max_length=56)
    location = models.CharField(max_length=56)
    unique_id = models.CharField(max_length = 10,unique=True,blank=True)
    plant = models.ManyToManyField(Plant,blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Device ID: {self.unique_id}"