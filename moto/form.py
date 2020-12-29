from django import forms
from django.forms import ModelForm
from moto.models import Moto
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


class MotoForm(ModelForm):
    # ID_Moto = forms.IntegerField(label="Reference ID", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))
    #
    date_entree = forms.DateField(label="Date d'entrée", widget=forms.DateInput(
        attrs={'type': 'date', 'max': 'today', 'id': "dateEntree"}), required=False,localize=False)

    date_vente = forms.DateField(label="Date de vente", widget=forms.DateInput(
        attrs={'type': 'date', 'max': 'today', 'id': "dateVente"}), required=False,localize=True)

    PA = Thousands(
        label='PA [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput()
    )
    PV = Thousands(
        label='PV [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput()
    )

    montant_reparation = Thousands(
        label='Montant de réparation',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput()
    )

    def __init__(self, *args, **kwargs):
        super(MotoForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control w3-margin-bottom',
            })
            if name != "ID_Moto" and name != "num_moteur":
                self.fields[name].required = False
            else:
                self.fields[name].required = True

            if name == "num_sur_facture":
                self.fields[name].label = "Num facture"

    class Meta:
        model = Moto

        fields = ['ID_Moto', 'date_entree', 'nom_moto', 'num_moteur', 'FRN', 'PA', 'PV', 'date_vente', 'nom_client_1','CIN_Num_Client_1', 'PJ_CIN_Client_1_recto', 'PJ_CIN_Client_1_verso',
                  'tel_client_1', 'num_BL', 'num_sur_facture', 'PJ_Facture', 'nom_client_2', 'tel_client_2', 'CIN_Num_Client_2', 'PJ_CIN_Client_2_recto', 'PJ_CIN_Client_2_verso', 'montant_reparation', 'motif_reparation', 'commercial']

class MotoFormCom(ModelForm):
    # ID_Moto = forms.IntegerField(label="Reference ID", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))
    #
    date_entree = forms.DateField(label="Date d'entrée", widget=forms.DateInput(
        attrs={'type': 'date', 'max': 'today', 'id': "dateEntree"}), required=False,localize=False)

    date_vente = forms.DateField(label="Date de vente", widget=forms.DateInput(
        attrs={'type': 'date', 'max': 'today', 'id': "dateVente"}), required=False,localize=True)

    PV = Thousands(
        label='PV [Ar]',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput()
    )

    montant_reparation = Thousands(
        label='Montant de réparation',
        label_suffix=False,
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput()
    )

    def __init__(self, *args, **kwargs):
        super(MotoFormCom, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control w3-margin-bottom',
            })
            if name != "ID_Moto" and name != "num_moteur":
                self.fields[name].required = False
            else:
                self.fields[name].required = True
                
            if name == "num_sur_facture":
                self.fields[name].label = "Num facture"
    class Meta:
        model = Moto

        fields = ['ID_Moto', 'date_entree', 'nom_moto', 'num_moteur', 'FRN','PV', 'date_vente', 'nom_client_1','CIN_Num_Client_1', 'PJ_CIN_Client_1_recto', 'PJ_CIN_Client_1_verso',
                  'tel_client_1', 'num_BL', 'num_sur_facture','PJ_Facture', 'nom_client_2', 'tel_client_2','CIN_Num_Client_2', 'PJ_CIN_Client_2_recto', 'PJ_CIN_Client_2_verso', 'montant_reparation', 'motif_reparation','commercial']
