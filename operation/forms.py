from django import forms
from django.forms import ModelForm
from .models import Operation
from importateur.models import Importateur
from exportateur.models import Exportateur

class preparationForm(ModelForm):
    Date_OT = forms.DateField(label="Date OT", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "DateOT"}),required=False)

    def __init__(self, *args, **kwargs):
        super(preparationForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            if name != "Date_OT":
                self.fields[name].widget.attrs.update({
                    'class': 'form-control w3-margin-bottom',
                })
                self.fields[name].required = False

        # label
        self.fields["Montant_Invoice"].label = "Montant Invoice"
        self.fields["Invoice_PJ"].label = "Pièce jointe Invoice"
        self.fields["Invoice_Num"].label = "Numéro Invoice"
        self.fields["Nbre_Colis"].label = "Nombre de colis"
        self.fields["PJ_PL"].label = "Pièce jointe Packing List"
        self.fields["Gross_Weight"].label = "Gross weight"
        self.fields["Net_Weight"].label = "Net weight"
        self.fields["DE_Num"].label = "Numero DE"
        self.fields["DE_PJ"].label = "Pièce jointe DE"
        self.fields["Fumigation_Num"].label = "Numero Fumigation"
        self.fields["Fumigation_PJ"].label = "Pièce jointe Fumigation"
        self.fields["Exportateur_Name"].label = "Nom de l'Exportateur"
        self.fields["BSC_ID_Exportateur"].label = "ID BSC Exportateur"
        self.fields["BSC_Num"].label = "Numero BSC"
        self.fields["Importateur_Name"].label = "Nom de l'Importateur"
        self.fields["BSC_ID_Importateur"].label = "ID BSC Importateur"
        self.fields["BSC_PJ"].label = "Pièce jointe BSC"
        self.fields["BSC_Remarque"].label = "Remarque"
        self.fields["BSC_Depense"].label = "Dépense"
        self.fields["Dom_Num"].label = "Numero domiciliation"
        self.fields["Dom_PJ"].label = "Pièce jointe domiciliation"
        self.fields["Dom_Banque"].label = "Banque de domiciliation"
        self.fields["Dom_Num_Compte"].label = "Numéro de compte"
        self.fields["Dom_Depense"].label = "Dépense"
        self.fields["OT_PJ"].label = "Pièce jointe"
        self.fields["Date_OT"].label = "Date OT"
        self.fields["OT_Honoraire"].label = "Honoraire"
        self.fields["Autres_Num"].label = "Numéro Autres"


        # specific id
        self.fields["Exportateur_Name"].widget.attrs.update({'id': 'Exportateur'})
        self.fields["BSC_ID_Exportateur"].widget.attrs.update({'id': 'ExportateurIdBSC'})
        self.fields["Importateur_Name"].widget.attrs.update({'id': 'Importateur'})
        self.fields["BSC_ID_Importateur"].widget.attrs.update({'id': 'ImportateurIdBSC'})
        self.fields["Dom_Banque"].widget.attrs.update({'id': 'DomBanque'})

    class Meta:
        model = Operation
        fields = ['INCOTERM','Montant_Invoice','Devise','Invoice_PJ','Invoice_Num','Nbre_Colis','PJ_PL','Gross_Weight','Net_Weight','DE_Num','DE_PJ','Fumigation_Num','Fumigation_PJ','Exportateur_Name','BSC_ID_Exportateur','BSC_Num','Importateur_Name','BSC_ID_Importateur','BSC_PJ','BSC_Remarque','BSC_Depense','Dom_Num','Dom_PJ','Dom_Banque','Dom_Num_Compte','Dom_Depense','OT_PJ','Date_OT','OT_Honoraire','Autres_Num','Champ_1','ch1_PJ','Champ_2','ch2_PJ','Champ_3','ch3_PJ','Champ_4','ch4_PJ','Autres_Depense'
        ]
