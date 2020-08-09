from django.db import models

# Create your models here.


class Caisse(models.Model):
    libellee = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, null=True)
    depense = models.IntegerField(default="0",null=False)
    recette = models.IntegerField(default="0",null=False)
    PJ = models.FileField(blank=True, upload_to='images')

    def __str__(self):
        return self.libellee

class Solde(models.Model):
    soldeInitial = models.IntegerField(default="0")
    soldeActuel = models.IntegerField(default="0")
