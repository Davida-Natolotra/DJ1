from django.db import models
from compagnie.models import Compagnie
from exportateur.models import Exportateur
from importateur.models import Importateur
# Create your models here.
class Operation(models.Model):
# Reception
#------------------------
    TYPEOP = (('Importation','Importation'),('Exportation','Exportation'))

    Date_Reception = models.DateField(auto_now=False,null=True)
    type_Operation = models.CharField(blank=True,max_length=50,choices=TYPEOP)
    Reference_Reception = models.CharField(blank=True,max_length=50)
    BL_PJ = models.FileField(blank=True,upload_to='operations')
    BL_Num = models.CharField(max_length=500,blank=True)
    BL_Date = models.DateField(auto_now=False,null=True)
    Container = models.CharField(max_length=500,blank=True)
    Plomb = models.CharField(max_length=500,blank=True)
    ETA = models.DateField(auto_now=False,null=True)
    Marchandise = models.CharField(max_length=500,blank=True)
    Poids = models.IntegerField(null=True,blank=True)
    Depart = models.DateField(auto_now=False,null=True)
    Arrivee_Tana = models.DateField(auto_now=False,null=True)
    Client = models.CharField(max_length=500,blank=True)

# Preparation
#-------------------------
    # Invoice
    INCOTERM = models.CharField(max_length=500,blank=True)
    Montant_Invoice = models.IntegerField(null=True,blank=True)
    Devise = models.IntegerField(null=True,blank=True)
    Invoice_PJ = models.FileField(blank=True,upload_to='operations')
    Invoice_Num = models.CharField(max_length=500,blank=True)

    # Packing list
    Nbre_Colis = models.IntegerField(blank=True,null=True)
    PJ_PL = models.FileField(blank=True,upload_to='operations')
    Gross_Weight = models.IntegerField(blank=True,null=True)
    Net_Weight = models.IntegerField(blank=True,null=True)

    # DE
    DE_Num = models.CharField(max_length=500,blank=True)
    DE_PJ = models.FileField(blank=True,upload_to='operations')

    # Fumigation
    Fumigation_Num = models.CharField(max_length=500,blank=True)
    Fumigation_PJ = models.FileField(blank=True,upload_to='operations')

    # BSC
    Exportateur_Name = models.ForeignKey(Exportateur, on_delete= models.CASCADE,null=True,blank=True)
    BSC_ID_Exportateur = models.CharField(max_length=500,blank=True)
    BSC_Num = models.CharField(max_length=500,blank=True)
    Importateur_Name = models.ForeignKey(Importateur,on_delete=models.CASCADE,null=True,blank=True)
    BSC_ID_Importateur = models.CharField(max_length=500,blank=True)
    BSC_PJ = models.FileField(blank=True,upload_to='operations')
    BSC_Remarque = models.CharField(max_length=500,blank=True)
    BSC_Depense = models.IntegerField(null=True,blank=True)

    # Domiciliation
    Dom_Num = models.CharField(max_length=500,blank=True)
    Dom_PJ = models.FileField(blank=True,upload_to='operations')
    Dom_Banque = models.CharField(max_length=500,blank=True)
    Dom_Num_Compte = models.CharField(max_length=500,blank=True)
    Dom_Depense = models.IntegerField(null=True,blank=True)

    # OT
    OT_PJ = models.FileField(blank=True,upload_to='operations')
    Date_OT = models.DateField(auto_now=False,null=True)
    OT_Honoraire = models.IntegerField(null=True,blank=True)

    # Autre
    Autres_Num = models.CharField(max_length=500,blank=True)
    Champ_1 = models.CharField(max_length=500,blank=True)
    Champ_2 = models.CharField(max_length=500,blank=True)
    Champ_3 = models.CharField(max_length=500,blank=True)
    Champ_4 = models.CharField(max_length=500,blank=True)
    ch1_PJ = models.FileField(blank=True,upload_to='operations')
    ch2_PJ = models.FileField(blank=True,upload_to='operations')
    ch3_PJ = models.FileField(blank=True,upload_to='operations')
    ch4_PJ = models.FileField(blank=True,upload_to='operations')
    Autres_Depense = models.IntegerField(null=True,blank=True)

    # Indicator notification
    Prep_Full = models.BooleanField(default=False)

# Dedouannement
#------------------------
    # Compagnie
        # Details
        #================
    Nom_Compagnie = models.ForeignKey(Compagnie,on_delete=models.CASCADE,null=True,blank=True)

        # BAD
        #-===============
    Date_BAD = models.DateField(auto_now=False,null=True)
    BAD_Montant = models.IntegerField(blank=True,null=True)
    BAD_PJ = models.FileField(blank=True,upload_to='operations')

        # Overstay
        #================
    Overstay_Nb_jrs = models.IntegerField(blank=True,null=True)
    Overstay_Montant = models.IntegerField(blank=True,null=True)
    Overstay_PJ = models.FileField(blank=True,upload_to='operations')

        # Surestaries
        #================
    Surestaries_Nb_jrs = models.IntegerField(blank=True,null=True)
    Surestaries_Montant = models.IntegerField(null=True,blank=True)
    Surestaries_PJ = models.FileField(blank=True,upload_to='operations')

    #  MICTSL/SMMC
        # Type d'operations
    OPMIC = (('Debarquement','Debarquement'),('Embarquement','Embarquement'))
    MICTSL_SMMC = models.CharField(blank=True,null=True,max_length=20,choices=OPMIC)
    Date_MICTSL = models.DateField(auto_now=False,null=True)
    Montant_MICTSL = models.IntegerField(blank=True,null=True)

        # Magasinage
    Magasinage_Nb_Jrs = models.IntegerField(blank=True,null=True)
    Magasinage_Montant = models.IntegerField(null=True,blank=True)
    Magasinage_PJ = models.FileField(blank=True,upload_to='operations')

    # Douane
        # DAU
        #================
    DAU_Date = models.DateField(auto_now=False,null=True)
    DAU_Num = models.CharField(max_length=500,blank=True)
    DAU_Depense = models.IntegerField(blank=True,null=True)
    CIRCOP = (('vert','Vert'),('jaune','Jaune'),('rouge','Rouge'))
    Circuit = models.CharField(blank=True,null=True,max_length=20,choices=CIRCOP)
    Date_Liquidation = models.DateField(auto_now=False,null=True)
    Liquidateur = models.CharField(blank=True,max_length=500)
    Resultat_Scan = models.CharField(blank=True,max_length=500)
    Resultat_Scan_PJ = models.FileField(blank=True,upload_to='scans')
    Resultat_Visite = models.FileField(blank=True,upload_to='visites')
    Droit_Compromis = models.IntegerField(blank=True,null=True)
    MODEPAIE = (('Cash','Cash'),('Virement banquaire','Virement banquaire'),('Cheque','Cheque'),('Western Union','Western Union'),('MVola','MVola'))
    DC_Mode_Paiement = models.CharField(blank=True,null=True,max_length=20,choices=MODEPAIE)
    Amende_Montant = models.IntegerField(blank=True,null=True)
    Amende_Mode_Paiement =  models.CharField(blank=True,null=True,max_length=20,choices=MODEPAIE)

        # OV
        #===================
    OV_Num = models.CharField(max_length=500,blank=True)
    OV_Montant = models.IntegerField(blank=True,null=True)
    OV_Date_Paiement = models.DateField(auto_now=False,null=True)
    OV_Banque = models.CharField(max_length=500,blank=True)
    OV_Num_Compte = models.CharField(max_length=500,blank=True,null=True)
    OV_Depense = models.IntegerField(blank=True,null=True)
    OV_Docker = models.IntegerField(blank=True,null=True)

        # Chargement
        #====================
    Date_Chargement = models.DateField(auto_now=False,null=True)
    Num_Camion = models.CharField(max_length=50, blank=True)
    Num_Remorque = models.CharField(max_length=50, blank=True)
    Nom_Transporteur = models.CharField(max_length=500, blank=True)
    Nom_Chauffeur = models.CharField(max_length=500, blank=True)
    Tel_Chauffeur = models.CharField(max_length=500, blank=True)
    Num_Permis = models.CharField(max_length=500, blank=True)
    Lieu_Livraison = models.CharField(max_length=500, blank=True)
    Montant_Fret = models.IntegerField(blank=True,null=True)
    Immobilisation = models.IntegerField(blank=True,null=True)
    Autres_Motifs = models.CharField(max_length=500,blank=True)
    Autres_Montant = models.IntegerField(blank=True,null=True)

        # Bon de sortie
        #====================
    Num_BS = models.CharField(max_length=500,blank=True)
    Date_BS = models.DateField(auto_now=False,null=True)
    Date_Livraison = models.DateField(auto_now=False,null=True)
    Remarque_General = models.CharField(max_length=500,blank=True)

        # Depense
        #=====================
    Depense_Fixe = models.IntegerField(blank=True,null=True)
    Depense_Autre = models.IntegerField(blank=True,null=True)

    # Total
    #=========
    Total = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.Reference_Reception
