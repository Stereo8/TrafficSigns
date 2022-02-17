from pyexpat import model
from django.db import models

# Create your models here.



class Pitanje(models.Model):
    znak = models.CharField(max_length=150, null=True, blank=True)
    opis = models.CharField(max_length=150, null=True, blank=True)
    tacan_odg = models.CharField(max_length=150)
    netacni_odg1 = models.CharField(max_length=150)
    netacni_odg2 = models.CharField(max_length=150)
