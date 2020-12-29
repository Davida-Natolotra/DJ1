from django import forms
from django.forms import ModelForm
from .models import Solde

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


class SoldeForm(ModelForm):
    soldeInitial = Thousands(
        label='Dépense [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','value':'0'}),required=False
    )

    soldeActuel = Thousands(
        label='Dépense [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','value':'0'}),required=False
    )

    class Meta:
        model = Solde
        localized_fields = '__all__'
        fields = ['soldeInitial','soldeActuel']
