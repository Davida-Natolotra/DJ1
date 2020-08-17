from django.db import models
from operation.models import Operation
# Create your models here.
class FactureOperation(models.Model):
    idOp = models.ForeignKey(Operation,on_delete=models.CASCADE)
    OT_Honoraire = models.IntegerField(default=0,blank=True,null=True)
    Autres_Montant = models.IntegerField(default=0,blank=True,null=True)
    BAD_Montant = models.IntegerField(default=0,blank=True,null=True)
    Overstay_Montant = models.IntegerField(blank=True,null=True)
    Surestaries_Montant = models.IntegerField(blank=True,null=True)
    Debarquement = models.IntegerField(blank=True,null=True)
    Magasinage_Montant = models.IntegerField(blank=True,null=True)
    Droit_Compromis = models.IntegerField(blank=True,null=True)
    Amende_Montant = models.IntegerField(blank=True,null=True)
    OV_Montant = models.IntegerField(blank=True,null=True)
    OV_Docker = models.IntegerField(blank=True,null=True)
    Montant_Fret = models.IntegerField(blank=True,null=True)
    Immobilisation = models.IntegerField(blank=True,null=True)
    Num_Facture = models.CharField(max_length=50,blank=True)
    Nom_Client = models.CharField(max_length=500,blank=True)
    Adresse_Client = models.CharField(max_length=500,blank=True)
    Contact_Client = models.CharField(max_length=500,blank=True)
    email_client = models.EmailField(max_length=500,blank=True)
    Date_Facture = models.DateField(auto_now=False,blank=True)
    SousTotal = models.IntegerField(blank=True,null=True)
    Tax = models.IntegerField(blank=True,null=True)
    TotalFacture = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.Nom_Client
