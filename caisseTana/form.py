from django import forms
from django.forms import ModelForm
from .models import Caisse

from django.core.exceptions import ValidationError
from decimal import Decimal, DecimalException
from django.utils import formats
from django.utils.encoding import force_text


class Thousands(forms.DecimalField):
    def to_python(self, value):
        if value in self.empty_values:
            return None
        if self.localize:
            value = formats.sanitize_separators(value)
        value = force_text(value).strip().replace(' ', '')

        try:
            value = Decimal(value)
        except DecimalException:
            raise ValidationError(
                self.error_messages['invalid'], code='invalid')
        return value


class CaisseForm(ModelForm):
    libellee = forms.CharField(label='Libellee',
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}))

    date  = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "date"}),required=False)

    depense = Thousands(
        label='Dépense [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','value':'0'}),required=False
    )
    recette = Thousands(
        label='Recette [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','value':'0'}),required=False
    )


    PJ = forms.FileField(label="Piece jointe ", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    class Meta:
        model = Caisse
        localized_fields = '__all__'
        fields = ['libellee','date','depense','recette','PJ']
