from django.db import models

# Create your models here.


class Versement(models.Model):

    date = models.DateField(auto_now=False, null=True)
    reference = models.CharField(max_length=500)
    beneficiaire = models.CharField(max_length=500)
    montant = models.IntegerField(default="0",null=False)
    remarque = models.CharField(max_length=500)
    PJ = models.FileField(blank=True, upload_to='images')

    def __str__(self):
        return self.reference
