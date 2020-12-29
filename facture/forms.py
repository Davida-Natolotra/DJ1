from django import forms
from django.forms import ModelForm
from operation.models import Operation
from django.core.exceptions import ValidationError
from decimal import Decimal, DecimalException
from django.utils import formats
from django.utils.encoding import force_text
from moto.models import Moto
from .models import FactureMoto

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

class factureForm(ModelForm):
    Facture_Date_Facture = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today'}),required=False)

    Facture_OT_Honoraire = Thousands(label='OT - Honoraire',max_digits=20, decimal_places=2, widget=forms.TextInput())

    Facture_Autres_Montant = Thousands(label='Autres montant',max_digits=20, decimal_places=2, widget=forms.TextInput())

    Facture_BAD_Montant = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Overstay_Montant = Thousands(label='Overstay',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Surestaries_Montant = Thousands(label='Surestaries',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Debarquement = Thousands(label='Debarquement',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Magasinage_Montant = Thousands(label='Magasinage',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Droit_Compromis = Thousands(label='Droit compromis',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Amende_Montant = Thousands(label='Amende',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_OV_Montant = Thousands(label='OV',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_OV_Docker = Thousands(label='Docker',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Montant_Fret = Thousands(label='Fret',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_Immobilisation = Thousands(label='Immobilisation',max_digits=20,decimal_places=2, widget=forms.TextInput())

    Facture_SousTotal = Thousands(max_digits=20,decimal_places=2, widget=forms.TextInput())

    TotalFacture = Thousands(max_digits=20,decimal_places=2, widget=forms.TextInput())
    Tax = Thousands(max_digits=20,decimal_places=2, widget=forms.TextInput())


    def __init__(self, *args, **kwargs):
        super(factureForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            if name != 'Facture_Date_Facture':
                self.fields[name].widget.attrs.update({'class': 'form-control'})
                self.fields[name].required = False

    class Meta:
        model = Operation
        fields = [
            'Facture_OT_Honoraire','Facture_Autres_Montant','Facture_BAD_Montant','Facture_Overstay_Montant','Facture_Surestaries_Montant','Facture_Debarquement','Facture_Magasinage_Montant','Facture_Droit_Compromis','Facture_Amende_Montant','Facture_OV_Montant','Facture_OV_Docker','Facture_Montant_Fret','Facture_Immobilisation','Facture_Num_Facture','Facture_Nom_Client','Facture_Adresse_Client','Facture_Contact_Client','Facture_email_client','Facture_Date_Facture','Facture_SousTotal','Tax','TotalFacture'
        ]


class factureMotoForm(ModelForm):
    """docstring for factureMoto."""
    PU_HT = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    TVA = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    PV = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    date_vente = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today'}),required=False)
    num_sur_facture = forms.CharField(label="Num facture",widget=forms.TextInput())
    def __init__(self, *args, **kwargs):
        super(factureMotoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            if name != 'Facture_Date_Facture':
                self.fields[name].widget.attrs.update({'class': 'form-control'})
                self.fields[name].required = False

    class Meta:
        model = Moto
        fields = [
        'nom_client_2','CIN_Num_Client_2','adresse_client_2','tel_client_2','volume_moteur','PU_HT','TVA','PT','montant_lettre','PV','date_vente','Ref','num_sur_facture'
        ]

class BLMotoForm(ModelForm):
    """docstring for factureMoto."""
    PU_HT = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    TVA = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    PV = Thousands(label='BAD',max_digits=20,decimal_places=2, widget=forms.TextInput())
    date_vente = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today'}),required=False)
    num_BL= forms.CharField(label="Num BL",widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(BLMotoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            if name != 'Facture_Date_Facture':
                self.fields[name].widget.attrs.update({'class': 'form-control'})
                self.fields[name].required = False

    class Meta:
        model = Moto
        fields = [
        'nom_client_1','CIN_Num_Client_1','adresse_client_1','tel_client_1','volume_moteur','PU_HT','TVA','PT','montant_lettre','PV','date_vente','Ref','num_BL'
        ]
