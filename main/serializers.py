from rest_framework import serializers
from django.contrib.auth.models import User
from main import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = ['building_country',
                  'building_county',
                  'building_city',
                  'building_street',
                  'building_zip_code',
                  'building_offices']

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Office
        fields = ['office_building',
                  'office_free_spots',
                  'office_floor',
                  'office_hardware']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['profile_user',
                  'profile_office_located',
                  'profile_age',
                  'profile_gender',
                  'profile_birth_date',
                  'profile_nationality',
                  'profile_address']

class Work_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work_request
        fields = ['work_request_type',
                  'work_request_reason',
                  'work_request_building',
                  'work_request_user']