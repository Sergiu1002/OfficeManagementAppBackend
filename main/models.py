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

class birouri(models.Model):
    locuri_totale_birouri = models.PositiveIntegerField(null=True, blank=True)
    etaj_birouri = models.PositiveIntegerField(null=True, blank=True)
    hardware_birouri = models.TextField()

class cereri(models.Model):
    tip_cerere = models.CharField(max_length=150)
    motiv_cerere = models.TextField()

class cladiri(models.Model):
    tara_cladire = models.CharField(max_length=100)
    judet_cladire = models.CharField(max_length=100)
    oras_cladire = models.CharField(max_length=100)
    strada_cladire = models.CharField(max_length=100)
    cod_postal_cladire = models.CharField(max_length=100)
    nr_birouri_cladire = models.PositiveIntegerField(null=True, blank=True)

