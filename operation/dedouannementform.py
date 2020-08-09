from django import forms
from django.forms import ModelForm
from .models import Operation
from compagnie.models import Compagnie

class dedouannementForm(ModelForm):
    Date_BAD = forms.DateField(label="Date BAD", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_BAD"}),required=False)

    Date_MICTSL = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_MICTSL"}),required=False)

    DAU_Date = forms.DateField(label="Date DAU", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "DAU_Date"}),required=False)

    Date_Liquidation = forms.DateField(label="Date de liquidation", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_Liquidation"}),required=False)

    OV_Date_Paiement = forms.DateField(label="Date de paiement", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "OV_Date_Paiement"}),required=False)

    Date_Chargement = forms.DateField(label="Date de chargement", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_Chargement"}),required=False)

    Date_BS = forms.DateField(label="Date BS", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_BS"}),required=False)

    Date_Livraison = forms.DateField(label="Date de départ pour livraison", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "Date_Livraison"}),required=False)

    def __init__(self,*args,**kwargs):
        super(dedouannementForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            if name != "Date_BAD" and name != "Date_MICTSL" and name != "DAU_Date" amd name != "Date_Liquidation" and name != "OV_Date_Paiement" and name != "Date_Chargement" and name != "Date_BS" and name != "Date_Livraison":
                self.fields[name].widget.attrs.update({'class':'form-control w3-margin-bottom'})
                self.fields[name].required = False

        # label
        self.fields["Nom_Compagnie"].label = "Nom de la compagnie"
        self.fields["BAD_Montant"].label = "Montant BAD [Ar]"
        self.fields["BAD_PJ"].label = "Pièce jointe BAD"
        self.fields["Overstay_Nb_jrs"].label = "Nombre de jours"
        self.fields["Overstay_Montant"].label = "Montant [Ar]"
        self.fields["Overstay_PJ"].label = "Pièce jointe Overstay "
        self.fields["Surestaries_Nb_jrs"].label = "Nombre de jours"
        self.fields["Surestaries_Montant"].label = "Montant"
        self.fields["Surestaries_PJ"].label = "Pièce jointe Surestaries "
        self.fields["MICTSL_SMMC"].label = "Type d'operation"
        self.fields["Montant_MICTSL"].label = "Montant [Ar]"
        self.fields["Magasinage_Nb_Jrs"].label = "Nombre de jours"
        self.fields["Magasinage_Montant"].label = "Montant [Ar]"
        self.fields["Magasinage_PJ"].label = "Pièce jointe"
        self.fields["DAU_Num"].label = "Numero DAU"
        self.fields["DAU_Depense"].label = "Depense DAU [Ar]"
        self.fields["Circuit"].label = "Circuit"
        self.fields["Liquidateur"].label = "Inspecteur liquidateur"
        self.fields["Resultat_Scan"].label = "Résultat de scan"
        self.fields["Resultat_Scan_PJ"].label = "Pièce jointe"
        self.fields["Resultat_Visite"].label = "Résultat visite"
        self.fields["Droit_Compromis"].label = "Droit compromis"
        self.fields["DC_Mode_Paiement"].label = "Mode de paiement"
        self.fields["Amende_Montant"].label = "Montant [Ar]"
        self.fields["Amende_Mode_Paiement"].label = "Mode de paiement"
        self.fields["OV_Num"].label = "Numero OV"
        self.fields["OV_Montant"].label = "Montant [Ar]"
        self.fields["OV_Banque"].label = "Banque"
        self.fields["OV_Num_Compte"].label = "Numero de compte"
        self.fields["OV_Depense"].label = "Dépense [Ar]"
        self.fields["OV_Docker"].label = "Docker [Ar]"
        self.fields["Num_Camion"].label = "Numéro du camion"
        self.fields["Num_Remorque"].label = "Numéro de la remorque"
        self.fields["Nom_Transporteur"].label = "Nom du transporteur"
        self.fields["Nom_Chauffeur"].label = "Nom du chauffeur"
        self.fields["Tel_Chauffeur"].label = "Tel. chauffeur"
        self.fields["Num_Permis"].label = "Numéro du permis"
        self.fields["Lieu_Livraison"].label = "Lieu de livraison"
        self.fields["Montant_Fret"].label = "Montant du fret [Ar]"
        self.fields["Immobilisation"].label = "Immobilisation [Ar]"
        self.fields["Autres_Motifs"].label = "Motifs"
        self.fields["Autres_Montant"].label = "Montant [Ar]"
        self.fields["Num_BS"].label = "Numéro du bon de sortie"
        self.fields["Remarque_General"].label = "Remarque générale"
        self.fields["Depense_Fixe"].label = "Depense fixe"
        self.fields["Depense_Autre"].label = "Autre dépense"


        # specific id
        self.fields["Nom_Compagnie"].widget.attrs.update({'id': 'Compagnie'})

    class Meta:
        model = Operation
        fields = [
            'Nom_Compagnie','Date_BAD','BAD_Montant','BAD_PJ','Overstay_Nb_jrs','Overstay_Montant','Overstay_PJ','Surestaries_Nb_jrs','Surestaries_Montant','Surestaries_PJ','MICTSL_SMMC','Date_MICTSL','Montant_MICTSL','Magasinage_Nb_Jrs','Magasinage_Montant','Magasinage_PJ','DAU_Date','DAU_Num','DAU_Depense','Circuit','Date_Liquidation','Liquidateur','Resultat_Scan','Resultat_Scan_PJ','Resultat_Visite','Droit_Compromis','DC_Mode_Paiement','Amende_Montant','Amende_Mode_Paiement','OV_Num','OV_Montant','OV_Date_Paiement','OV_Banque','OV_Num_Compte','OV_Depense','OV_Docker','Date_Chargement','Num_Camion','Num_Remorque','Nom_Transporteur','Nom_Chauffeur','Tel_Chauffeur','Num_Permis','Lieu_Livraison','Montant_Fret','Immobilisation','Autres_Motifs','Autres_Montant','Num_BS','Date_BS','Date_Livraison','Remarque_General','Depense_Fixe','Depense_Autre','Total'
        ]
