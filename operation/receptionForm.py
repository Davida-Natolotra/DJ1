from django import forms
from django.forms import ModelForm
from operation.models import Operation

class ReceptionForm(ModelForm):
    Date_Reception = forms.DateField(label="Date de reception", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateReception"}),required=False)

    # iterable


    Reference_Reception = forms.IntegerField(label="Reference ID", widget=forms.NumberInput(attrs={'class':'form-control w3-margin-bottom'}))

    BL_PJ = forms.FileField(label="PJ BL", required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control-file w3-margin-bottom'}))

    BL_Num = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    BL_Date = forms.DateField(label="Date BL", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateBL"}),required=False)

    Container = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    Plomb = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    ETA = forms.DateField(label="Date BL", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateEntree"}),required=False)

    Marchandise = forms.CharField(label='Num BL',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    Poids = forms.IntegerField(label="Poids [Kg]", widget=forms.TextInput(attrs={'class':'form-control w3-margin-bottom','type':'number'}),required=False,localize=True)

    Depart = forms.DateField(label="Date de depart", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "dateDepart"}),required=False)

    Arrivee_Tana = forms.DateField(label="Date d'arrivee Tana", widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom','max': 'today', 'id': "arriveeTana"}),required=False)

    Client = forms.CharField(label='Client',
    widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'}),required=False)

    def __init__(self,*args,**kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            if name == "type_Operation":
                self.fields[name].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Operation
        fields = [
        'Date_Reception','type_Operation','Reference_Reception','BL_PJ','BL_Num','BL_Date','Container','Plomb','ETA','Marchandise','Poids','Depart','Arrivee_Tana','Client'
        ]
