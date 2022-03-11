from django.db import models
from django.utils import timezone

class angajati(models.Model):
    nume = models.CharField(max_length=15)
    prenume = models.CharField(max_length=15)
    varsta = models.PositiveIntegerField(null=True, blank=True)

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER = [
        (MALE, 'M'),
        (FEMALE, 'F'),
        (OTHER, 'O'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=MALE,)
    
    email = models.EmailField()
    data_nasterii = models.DateTimeField(auto_now=False, auto_now_add=False, default = timezone.now)
    nationalitate = models.CharField(max_length=45)
    adresa = models.CharField(max_length=100)

    def __int__(self):
        return self.pk

#class birouri(models.Model):
