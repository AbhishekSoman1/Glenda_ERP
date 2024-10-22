from django.db import models

from production_app.models import water_Finished_Goods


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=200, null=True)
    vehicle_nbr = models.CharField(max_length=200, null=True)
    vehicle_img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f"{self.vehicle_name} ({self.vehicle_nbr})"




from django.db import models
import requests

class Route(models.Model):
    route_name = models.CharField(max_length=200, null=True)
    starting_point = models.CharField(max_length=200, null=True)
    ending_point = models.CharField(max_length=200, null=True)
    total_distance = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.route_name

class Route_Plan(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE,null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE,null=True)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.route} - {self.driver} on {self.date} at {self.time}"



class Driver(models.Model):
    driver_name = models.CharField(max_length=200, null=True)
    license_number = models.CharField(max_length=200, null=True)
    aadhaar_number = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.driver_name

class logistics_report(models.Model):
    date = models.DateField(null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    stock = models.ForeignKey(water_Finished_Goods, on_delete=models.CASCADE, null=True )