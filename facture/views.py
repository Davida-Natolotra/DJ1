from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from operation.models import Operation
from .forms import factureForm, factureMotoForm, BLMotoForm
from operation.receptionForm import ReceptionForm
from moto.models import Moto
from facture.models import FactureMoto, BLMoto
# Create your views here.

def editFacture(request, id=None):
    operation = get_object_or_404(Operation, pk=id)
    if request.method == 'POST':
        form = factureForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            message = "success"
        else:
            message = "error"
    else:
        form = factureForm(instance=operation)
        recform = ReceptionForm(instance=operation)
        message = "new"

    return render(request, 'facture/edit.html', {'form': form,'id':operation.id,'message':message})


def previewFacture(request, id=None):
    Facture = get_object_or_404(Operation, pk=id)
    return render(request, 'facture/preview.html', {'Facture': Facture,'id':Facture.id,'client':Facture.Facture_Nom_Client})

def initFacture(request):
    if request.is_ajax and request.method == 'GET':
        id = request.GET.get("id",None)
        print("id = ",id)
        curOp = Operation.objects.get(pk=id)
        Facture_OT_Honoraire = curOp.OT_Honoraire
        print("Facture_OT_Honoraire = ",Facture_OT_Honoraire)
        Facture_Autres_Montant = curOp.Autres_Montant
        Facture_BAD_Montant = curOp.BAD_Montant
        Facture_Overstay_Montant = curOp.Overstay_Montant
        Facture_Surestaries_Montant = curOp.Surestaries_Montant
        Facture_Debarquement = curOp.Montant_MICTSL
        Facture_Magasinage_Montant = curOp.Magasinage_Montant
        Facture_Droit_Compromis = curOp.Droit_Compromis
        Facture_Amende_Montant = curOp.Amende_Montant
        Facture_OV_Montant = curOp.OV_Montant
        Facture_OV_Docker = curOp.OV_Docker
        Facture_Montant_Fret = curOp.Montant_Fret
        Facture_Immobilisation = curOp.Immobilisation
        Facture_Nom_Client = curOp.Client

        return JsonResponse({'Facture_OT_Honoraire':Facture_OT_Honoraire,'Facture_Autres_Montant':Facture_Autres_Montant,'Facture_BAD_Montant':Facture_BAD_Montant,'Facture_Overstay_Montant':Facture_Overstay_Montant,'Facture_Surestaries_Montant':Facture_Surestaries_Montant,'Facture_Debarquement':Facture_Debarquement,'Facture_Magasinage_Montant':Facture_Magasinage_Montant,'Facture_Droit_Compromis':Facture_Droit_Compromis,'Facture_Amende_Montant':Facture_Amende_Montant,'Facture_OV_Montant':Facture_OV_Montant,'Facture_OV_Docker':Facture_OV_Docker,'Facture_Montant_Fret':Facture_Montant_Fret,'Facture_Immobilisation':Facture_Immobilisation,'Facture_Nom_Client':Facture_Nom_Client},status=200)

def editFactureMoto(request,id=None):
    moto = get_object_or_404(Moto,pk=id)
    pageTitle = "Moto n°"+str(id)

    if request.method == 'POST':
        form = factureMotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            messages.success(request, "success")
        else:
            messages.error(request,'error')
    else:
        form = factureMotoForm(instance=moto)
    return render(request, 'facture/editFacture/editFactureMoto.html', {'form': form, 'moto': moto, 'pageTitle': pageTitle})

def editBLMoto(request,id=None):
    moto = get_object_or_404(Moto,pk=id)
    numBLlast = BLMoto.objects.last()
    pageTitle = "Moto n°"+str(id)
    if request.method == 'POST':
        form = BLMotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            messages.success(request,'success')
        else:
            messages.error(request,'error')
    else:
        form = BLMotoForm(instance=moto)

        message = "new"
    return render(request,'facture/editBL/editBLMoto.html',{'form':form,'moto':moto,'pageTitle':pageTitle})

def previewFactureMoto(request, id=None):
    Facture = get_object_or_404(Moto, pk=id)
    pageTitle = "Moto n°"+str(Facture.ID_Moto)
    return render(request, 'facture/previewFacture/previewFactureMoto.html', {'Facture': Facture,'pageTitle':pageTitle})

def previewBLMoto(request, id=None):
    Facture = get_object_or_404(Moto, pk=id)
    pageTitle = "Moto n°"+str(Facture.ID_Moto)
    return render(request, 'facture/previewBL/previewBLMoto.html', {'Facture': Facture,'pageTitle':pageTitle})
