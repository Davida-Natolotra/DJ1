from django.db import models

# Create your models here.
class Compagnie(models.Model):
    nomCompagnie = models.CharField(max_length=500)
    adresseTana = models.CharField(max_length=500)
    adresseTamatave = models.CharField(max_length=500)
    email1 = models.EmailField()
    email2 = models.EmailField()
    email3 = models.EmailField()
    contact = models.CharField(max_length=500)
