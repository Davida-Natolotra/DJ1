from django.db import models

# Create your models here.
class Moto(models.Model):
    ID_Moto = models.IntegerField(blank=True)
    date_entree = models.DateField(auto_now=False,blank=True,null=True)
    nom_moto = models.CharField(max_length=500)
    num_moteur = models.CharField(max_length=500)
    FRN = models.CharField(max_length=500,blank=True)
    PA = models.IntegerField(null=True)
    PV = models.IntegerField(null=True)
    date_vente = models.DateField(auto_now=False,null=True)
    nom_client_1 = models.CharField(max_length=50, blank=True)
    PJ_CIN_Client_1_recto = models.FileField(blank=True,upload_to='images')
    PJ_CIN_Client_1_verso = models.FileField(blank=True,upload_to='images')
    tel_client_1 = models.CharField(max_length=50, blank=True)
    num_BL = models.CharField(max_length=500, blank=True)
    num_sur_facture = models.CharField(max_length=500, blank=True)
    nom_client_2 = models.CharField(max_length=50, blank=True)
    tel_client_2 = models.CharField(max_length=50, blank=True)
    PJ_CIN_Client_2_recto = models.FileField(blank=True,upload_to='images')
    PJ_CIN_Client_2_verso = models.FileField(blank=True,upload_to='images')
    montant_reparation = models.IntegerField(null=True)
    motif_reparation = models.TextField(blank=True)

    def __str__(self):
        return self.nom_moto
