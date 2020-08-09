from django import forms
from django.forms import ModelForm
from compagnie.models import Compagnie

class CompagnieForm(ModelForm):
    nomCompagnie = forms.CharField(label="Nom de la compagnie",required=False,
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    adresseTana = forms.CharField(label="Adresse Tana",required=False,
        widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}))

    adresseTamatave = forms.CharField(label="Adresse Tamatave",required=False,
        widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}))

    email1 = forms.EmailField(label="Email 1",required=False,
        widget= forms.EmailInput(attrs={'class': 'form-control w3-margin-bottom'}))

    email2 = forms.EmailField(label="Email 2",required=False,
        widget= forms.EmailInput(attrs={'class': 'form-control w3-margin-bottom'}))

    email3 = forms.EmailField(label="Email 3",required=False,
        widget= forms.EmailInput(attrs={'class': 'form-control w3-margin-bottom'}))

    contact = forms.CharField(label="Contact",required=False,
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    class Meta:
        model = Compagnie
        fields = [
        'nomCompagnie','adresseTana','adresseTamatave','email1','email2','email3','contact'
        ]
