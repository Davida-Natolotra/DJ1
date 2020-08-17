from django import forms
from django.forms import ModelForm
from operation.models import Operation


class factureForm(ModelForm):
    Facture_Date_Facture = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': 'today'}))

    def __init__(self, *args, **kwargs):
        super(factureForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control'})
            self.fields[name].required = False

    class Meta:
        model = Operation
        fields = [
            'Facture_OT_Honoraire','Facture_Autres_Montant','Facture_BAD_Montant','Facture_Overstay_Montant','Facture_Surestaries_Montant','Facture_Debarquement','Facture_Magasinage_Montant','Facture_Droit_Compromis','Facture_Amende_Montant','Facture_OV_Montant','Facture_OV_Docker','Facture_Montant_Fret','Facture_Immobilisation','Facture_Num_Facture','Facture_Nom_Client','Facture_Adresse_Client','Facture_Contact_Client','Facture_email_client','Facture_Date_Facture','Facture_SousTotal','Tax','TotalFacture'
        ]
