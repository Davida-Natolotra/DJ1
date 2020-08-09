from django import forms
from django.forms import ModelForm
from operation.models import Operation
from exportateur.models import Exportateur
from importateur.models import Importateur

class PreparationForm(ModelForm):
    INCOTERM = forms.CharField(label='INCOTERM',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    Montant_Invoice = forms.IntegerField(label="Montant invoice", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    # iterable
    TYPE_CHOICES_DEVISE =(
        ("1", "USD"),
        ("2", "EUR"),
    )
    Devise = forms.ChoiceField(choices = TYPE_CHOICES_DEVISE,label="Devise", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}),required=False)

    Invoice_PJ = forms.FileField(label="PJ Invoice", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    Invoice_Num = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    Nbre_Colis = forms.IntegerField(label="Nombre de colis", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    PJ_PL = forms.FileField(label="PJ Invoice", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    Gross_Weight = forms.IntegerField(label="Gross weight", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    Net_Weight = forms.IntegerField(label="Net weight", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    DE_Num = forms.CharField(label='Num DE',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    DE_PJ = forms.FileField(label="PJ DE", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    Fumigation_Num = forms.CharField(label='Num fumigation',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    Fumigation_PJ = forms.FileField(label="PJ Fumigation", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    # Exportateur_Name = forms.ModelChoiceField(queryset=...,label="Nom de l'exportateur",to_field_name="nom",widget= forms.ModelChoiceField(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    # BSC_ID_Exportateur = forms.CharField
    #
    # BSC_Num
    #
    # Importateur_Name
    #
    # BSC_ID_Importateur
    #
    # BSC_PJ
    #
    # BSC_Remarque
    #
    # BSC_Depense
    #
    # Dom_Num
    #
    # Dom_PJ
    #
    # Dom_Banque
    #
    # Dom_Num_Compte
    #
    # Dom_Depense
    #
    # OT_PJ
    #
    # Date_OT
    #
    # OT_Honoraire
    #
    # Autres_Num
    #
    # Champ_1
    #
    # Champ_2
    #
    # Champ_3
    #
    # Champ_4
    #
    # ch1_PJ
    #
    # ch2_PJ
    #
    # ch3_PJ
    #
    # ch4_PJ
    #
    # Autres_Depense

    class Meta():
        model = Operation
        fields = [
        'INCOTERM','Montant_Invoice','Devise','Invoice_PJ','Invoice_Num','Nbre_Colis','PJ_PL','Gross_Weight','Net_Weight','DE_Num','DE_PJ','Fumigation_Num','Fumigation_PJ',
        ]
