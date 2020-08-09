from django import forms
from django.forms import ModelForm
from .models import Solde

class SoldeForm(ModelForm):
    soldeInitial = forms.IntegerField(label="Solde initial [Ar]", widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','type':'number'}),required=False)

    soldeActuel = forms.IntegerField(label="Solde actuel [Ar]", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom','type':'number','disabled':''}),required=False)

    class Meta:
        model = Solde
        localized_fields = '__all__'
        fields = ['soldeInitial','soldeActuel']
