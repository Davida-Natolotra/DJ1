from django import forms
from django.forms import ModelForm
from .models import Caisse

class CaisseForm(ModelForm):
    libellee = forms.CharField(label='Libellee',
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    date  = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "date"}),required=False)

    depense = forms.IntegerField(label="Depense [Ar]", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number','value':'0'}),required=False)

    recette = forms.IntegerField(label="Recette [Ar]", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number','value':'0'}),required=False)

    PJ = forms.FileField(label="Piece jointe ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    class Meta:
        model = Caisse
        localized_fields = '__all__'
        fields = ['libellee','date','depense','recette','PJ']
