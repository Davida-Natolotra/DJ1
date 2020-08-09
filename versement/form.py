from django import forms
from django.forms import ModelForm
from versement.models import Versement

class VersementForm(ModelForm):
    date  = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "date"}),required=False)

    reference = forms.CharField(label='Reference',
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    beneficiaire = forms.CharField(label='Beneficiaire',
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    montant = forms.IntegerField(label="Montant [Ar]", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number','value':'0'}),required=False)

    remarque = forms.CharField(label='Remarque',
        widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}), required=False)

    PJ = forms.FileField(label="Piece jointe ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    class Meta:
        model = Versement
        fields = ['date','reference','beneficiaire','montant','remarque','PJ']
