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
    user = models.ForeignKey(User,models.CASCADE)
    unique_id = models.SlugField(max_length = 10,unique=True)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)

    def __str__(self):
        return f"Device ID: {unique_id}"