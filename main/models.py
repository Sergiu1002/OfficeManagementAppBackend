from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Office(models.Model):
    #office_building = models.ForeignKey(Building, on_delete=models.CASCADE)
    office_free_spots = models.PositiveIntegerField(null=True, blank=True)
    office_floor = models.PositiveIntegerField(null=True, blank=True)
    office_hardware = models.TextField()
    def __int__(self):
        return self.pk

class Work_request(models.Model):
    work_request_type = models.CharField(max_length=150)
    work_request_reason = models.TextField()
    def __int__(self):
        return self.pk

class Building(models.Model):

    building_country = models.CharField(max_length=100)
    building_county = models.CharField(max_length=100)
    building_city = models.CharField(max_length=100)
    building_street = models.CharField(max_length=100)
    building_zip_code = models.CharField(max_length=100)
    building_offices = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    profile_age = models.PositiveIntegerField(null=True, blank=True)

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER = [
        (MALE, 'M'),
        (FEMALE, 'F'),
        (OTHER, 'O'),
    ]
    profile_gender = models.CharField(max_length=1, choices=GENDER, default=MALE,)
    profile_birth_date = models.DateTimeField(auto_now=False, auto_now_add=False, default = timezone.now)
    profile_nationality = models.CharField(max_length=45)
    profile_address = models.CharField(max_length=100)
