from django import forms
from django.forms import ModelForm
from .models import Flower

class MyForm(ModelForm):
    title = forms.CharField(label='Title', 
        widget= forms.TextInput(attrs={'class': 'form-control w3-margin-bottom'})) 
    description = forms.CharField(label='Description',widget= forms.Textarea(attrs={'class': 'form-control w3-margin-bottom'}),required=False)
    datepick = forms.DateField(label="Date",widget=forms.DateInput(attrs={'type':'date','class':'form-control w3-margin-bottom'}))
    image = forms.ImageField(label='Piece jointe: ')
    class Meta:
        model = Flower
        fields = ['title','description','datepick','image']