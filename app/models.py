from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Donor Model
class DonorModel(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    last_donation_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.blood_type})"
    

#BloodInventoryModel
class BloodInventoryModel(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, unique=True)
    units_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.blood_type} - {self.units_available} units"
    

#BloodRequestModel
class BloodRequestModel(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    blood_type = models.CharField(max_length=3, choices=BloodInventoryModel.BLOOD_TYPES)
    units_requested = models.PositiveIntegerField()
    status = models.CharField(max_length=10, default='Pending')
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} requested {self.units_requested} units of {self.blood_type}"

    

