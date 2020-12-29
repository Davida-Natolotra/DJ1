from django.db import models
from operation.models import Operation
# Create your models here.
class FactureOperation(models.Model):
    idOp = models.ForeignKey(Operation,on_delete=models.CASCADE)
    OT_Honoraire = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Autres_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    BAD_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Overstay_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Surestaries_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Debarquement = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Magasinage_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Droit_Compromis = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Amende_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    OV_Montant = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    OV_Docker = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Montant_Fret = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Immobilisation = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Num_Facture = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Nom_Client = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Adresse_Client = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Contact_Client = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    email_client = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Date_Facture = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    SousTotal = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Tax = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    TotalFacture = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=20)
    Ref = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.Nom_Client

class FactureMoto(models.Model):
    Num_Facture = models.IntegerField(null=True,default=0)
    def __int__(self):
        return self.Num_Facture

class BLMoto(models.Model):
    Num_BL = models.IntegerField(null=True,default=0)
    def __int__(self):
        return self.Num_Facture
