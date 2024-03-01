from django.db import models
from django.contrib.auth import get_user_model

Users = get_user_model()

class Car(models.Model):
    Model = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Fueltype = models.CharField(max_length=100)
    Dailyrate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()


class Customer(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contactnumber = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self) -> str:
        return super().__str__()

class Rent(models.Model):
    Rent_Start = models.DateTimeField()
    Rend_End = models.DateTimeField()
    TotalCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()


class Maintenance(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Maintenance_date = models.DateTimeField()
    Description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()