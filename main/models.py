from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Building(models.Model):

    building_country = models.CharField(max_length=100)
    building_county = models.CharField(max_length=100)
    building_city = models.CharField(max_length=100)
    building_street = models.CharField(max_length=100)
    building_zip_code = models.CharField(max_length=100)
    building_offices = models.PositiveIntegerField(null=True, blank=True)
    building_floors = models.PositiveIntegerField(null=True, blank=True)

class Office(models.Model):
    office_building = models.ForeignKey(Building, on_delete=models.CASCADE, default= None)
    office_total_desks = models.PositiveIntegerField(null=True, blank=True)
    office_free_desks = models.PositiveIntegerField(null=True, blank=True)
    office_floor = models.PositiveIntegerField(null=True, blank=True)
    office_hardware = models.TextField()
    def __int__(self):
        return self.pk

class Profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    profile_office_located = models.ForeignKey(Office, on_delete=models.CASCADE)
    
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

class Work_request(models.Model):
    REMOTE = 'Remote'
    ONSITE = 'Onsite'
    CHANGE_OFFICE = 'Change_office'
    WORK_REQUEST_TYPE = [
        (REMOTE, 'Remote'),
        (ONSITE, 'Onsite'),
        (CHANGE_OFFICE, 'Change_office'),
    ]
    work_request_type = models.CharField(max_length=14, choices=WORK_REQUEST_TYPE, default=ONSITE,)
    work_request_reason = models.TextField()

    work_request_building = models.ForeignKey(Building, on_delete=models.CASCADE)
    work_request_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.pk