from django.shortcuts import render, get_object_or_404
from moto.models import Moto
from django.http import HttpResponseRedirect
from moto.form import MotoForm, MotoFormCom
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.contrib import messages
from facture.models import FactureMoto, BLMoto
from facture.forms import factureMotoForm, BLMotoForm
# Create your views here.
def indexcom(request):
    pageTitle = "TIA MOTO SARLU"
    motos = Moto.objects.all()
    counter = len(motos)
    return render(request, 'moto/index.html', {'motos': motos,'pageTitle':pageTitle,'counter':counter})

def createMotoCom(request):
    id = "nouvelle enregistrement"
    pageTitle = "Moto: nouvelle enregistrement"
    if request.method == 'POST':
        form = MotoFormCom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'create')
            lastmoto = Moto.objects.last()
            print("pk = ", lastmoto.pk)
            return redirect('editMotoCom', pk=lastmoto.pk)
        else:
            messages.error(request, 'error')
    else:
        form = MotoFormCom()
        messages.success(request,'new')
    return render(request, 'commercial/createmotocom.html', {'form': form,'id':id,'pageTitle':pageTitle})


def editMotoCom(request, pk=None):
    print("Edit moto")
    moto = get_object_or_404(Moto, pk=pk)
    id = moto.ID_Moto
    pageTitle = "Moto n°"+str(id)
    if request.method == 'POST':
        form = MotoFormCom(request.POST, request.FILES, instance=moto)

        if form.is_valid():
            form.save()
            messages.success(request,'success')
        else:
            messages.error(request,'error')
    else:
        form = MotoFormCom(instance=moto)

    return render(request, 'commercial/editmotocom.html', {'form': form,'id':id,'pageTitle':pageTitle})


def editFactureMotoCom(request, id=None):
    moto = get_object_or_404(Moto,pk=id)
    pageTitle = "Moto n°"+str(id)

    if request.method == 'POST':
        fac = FactureMoto.objects.last()
        numFacture = fac.Num_Facture
        print('numFacture = ',numFacture)
        numFacture = numFacture +1
        moto.num_sur_facture = numFacture
        fac.Num_Facture = numFacture
        fac.save()
        moto.save()
        form = factureMotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            messages.success(request, "success")
        else:
            messages.error(request,'error')
    else:
        form = factureMotoForm(instance=moto)
    return render(request, 'commercial/editfactmoto/edfactmotocom.html', {'form': form, 'moto': moto, 'pageTitle': pageTitle})


def editBLMotoCom(request, id=None):
    moto = get_object_or_404(Moto, pk=id)
    pageTitle = "Moto"
    if request.method == 'POST':
        bl = BLMoto.objects.last()
        numBL = bl.Num_BL
        print('numFacture = ', numBL)
        numBL = numBL + 1
        moto.num_BL = numBL
        bl.Num_BL = numBL
        bl.save()
        moto.save()
        form = BLMotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            messages.success(request, 'success')
        else:
            messages.error(request, 'error')
    else:
        form = BLMotoForm(instance=moto)

        message = "new"
    return render(request, 'commercial/editBLmoto/edBLmotocom.html', {'form': form, 'moto': moto, 'pageTitle': pageTitle})

def previewFactureMotoCom(request, id=None):
    Facture = get_object_or_404(Moto, pk=id)
    pageTitle = "Moto n°"+str(Facture.ID_Moto)
    return render(request, 'commercial/previewfacturemoto/prevfacmotocom.html', {'Facture': Facture, 'pageTitle': pageTitle})

def previewBLMotoCom(request, id=None):
    Facture = get_object_or_404(Moto, pk=id)
    pageTitle = "Moto n°"+str(Facture.ID_Moto)
    return render(request, 'commercial/previewBLmoto/prevBLmoto.html', {'Facture': Facture, 'pageTitle': pageTitle})
