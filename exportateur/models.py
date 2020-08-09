from django.db import models

# Create your models here.
class Exportateur(models.Model):
    nom = models.CharField(max_length=500)
    adresse = models.CharField(max_length=500)
    email = models.EmailField()
    NIF = models.CharField(max_length=500)
    NIF_PJ = models.FileField(blank=True,upload_to='images')
    STAT = models.CharField(max_length=500)
    STAT_PJ = models.FileField(blank=True,upload_to='images')
    RCS = models.CharField(max_length=500)
    RCS_PJ = models.FileField(blank=True,upload_to='images')
    ID_BSC = models.CharField(max_length=500)
    login = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    banque = models.CharField(max_length=500)
    numCompte = models.CharField(max_length=500)
    CIN_gerant = models.IntegerField(null=True)
    CIN_PJ = models.FileField(blank=True,upload_to='images')
    cachet = models.FileField(blank=True,upload_to='images')
    numTel = models.CharField(max_length=500)


    def __str__(self):
        return self.nom
