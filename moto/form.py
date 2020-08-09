from django import forms
from django.forms import ModelForm
from moto.models import Moto

class MotoForm(ModelForm):
    ID_Moto = forms.IntegerField(label="Reference ID", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    date_entree = forms.DateField(label="Date d'entree", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateEntree"}),required=False)

    nom_moto = forms.CharField(label='Nom de la moto',
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    num_moteur = forms.CharField(label='Numero du moteur',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    FRN = forms.CharField(label='FRN',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    PA = forms.IntegerField(label="PA [Ar]", widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','type':'number','pattern':'[0-9]+([\.,][0-9]+)?','lang':'fr','step':'0.01'}),required=False,localize=True)

    PV = forms.IntegerField(label="PV [Ar]", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number'}),required=False)

    date_vente = forms.DateField(label="Date de vente", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateVente"}),required=False)

    nom_client_1 = forms.CharField(label='Nom du client 1',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    PJ_CIN_Client_1_recto = forms.FileField(label="CIN client 1 recto ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    PJ_CIN_Client_1_verso = forms.FileField(label="CIN client 1 verso ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    tel_client_1 = forms.CharField(label='Tel du client 1',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    num_BL = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    num_sur_facture = forms.CharField(label='Numero sur facture',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    nom_client_2 = forms.CharField(label='Nom du client 2',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    tel_client_2 = forms.CharField(label='Tel du client 2',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    PJ_CIN_Client_2_recto = forms.FileField(label="CIN client 2 recto ", required=False,widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    PJ_CIN_Client_2_verso = forms.FileField(label="CIN client 2 verso ", required=False,widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    montant_reparation = forms.IntegerField(label="Montant de reparation  [Ar]",widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}),required=False)

    motif_reparation = forms.CharField(label='Motif de reparation',
    widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    class Meta:
        model = Moto

        fields = ['ID_Moto','date_entree','nom_moto','num_moteur','FRN','PA','PV','date_vente','nom_client_1','PJ_CIN_Client_1_recto','PJ_CIN_Client_1_verso','tel_client_1','num_BL','num_sur_facture','nom_client_2','tel_client_2','PJ_CIN_Client_2_recto','PJ_CIN_Client_2_verso','montant_reparation','motif_reparation']
