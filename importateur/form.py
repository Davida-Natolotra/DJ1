from django import forms
from django.forms import ModelForm
from importateur.models import Importateur

class ImportateurForm(ModelForm):
    nom = forms.CharField(label="Nom de l'importateur",required=False,
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    adresse = forms.CharField(label="Adresse de l'importateur",required=False,
        widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}))

    email = forms.EmailField(label="Email",required=False,
        widget= forms.EmailInput(attrs={'class': 'form-control w3-margin-bottom'}))

    NIF = forms.CharField(label="NIF",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    NIF_PJ = forms.FileField(label="NIF PJ ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    STAT = forms.CharField(label="STAT",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    STAT_PJ = forms.FileField(label="STAT PJ ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    RCS = forms.CharField(label="RCS",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    RCS_PJ = forms.FileField(label="RCS PJ ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    ID_BSC = forms.CharField(label="ID BSC",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    login = forms.CharField(label="Login",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    password = forms.CharField(label="Password",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    banque = forms.CharField(label="Banque",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    numCompte = forms.CharField(label="Numero de compte",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    CIN_gerant = forms.IntegerField(label="CIN gerant", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number'}),required=False)

    CIN_PJ = forms.FileField(label="CIN gerant piece jointe ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    cachet = forms.FileField(label="Cachet ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    numTel = forms.CharField(label="Numero de telephone",required=False,
            widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    class Meta:
        model = Importateur
        fields =[
        'nom','adresse','email','NIF','NIF_PJ','STAT','STAT_PJ','RCS','RCS_PJ','ID_BSC','login','password','banque','numCompte','CIN_gerant','CIN_PJ','cachet','numTel'
        ]
