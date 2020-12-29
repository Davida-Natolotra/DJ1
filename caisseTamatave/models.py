from django.db import models

# Create your models here.


class Caisse(models.Model):
    libellee = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, null=True)
    depense = models.DecimalField(null=True,default="0",decimal_places=2,max_digits=20)
    recette = models.DecimalField(null=True,default="0",decimal_places=2,max_digits=20)
    PJ = models.FileField(blank=True, upload_to='images')

    def __str__(self):
        return self.libellee

class Solde(models.Model):
    soldeInitial = models.DecimalField(null=True,default="0",decimal_places=2,max_digits=20)
    soldeActuel = models.DecimalField(null=True,default="0",decimal_places=2,max_digits=20)
