from django.contrib import admin
from .models import Profile, Office, Work_request, Building
# Register your models here.
admin.site.register(Profile)
admin.site.register(Office)
admin.site.register(Work_request)
admin.site.register(Building)
