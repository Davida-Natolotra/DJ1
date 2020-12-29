from django.shortcuts import render, get_object_or_404
from base.views import topbar
from .form import CaisseForm
from .models import Caisse, Solde
from .soldeForm import SoldeForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def indexTamatave(request):
    caisseTamataves = Caisse.objects.all()
    solde = Solde.objects.all()
    pageTitle = "Caisse Tamatave"
    return render(request,'caisseTamatave/index.html',{'caisseTamataves':caisseTamataves,'solde':solde,'pageTitle':pageTitle})

def refSoldeTamatave(request,pk=None):
    pageTitle = "Caisse Tamatave"
    solde = get_object_or_404(Solde, pk=pk)
    if request.method == 'POST':
        form = SoldeForm(request.POST,instance=solde)

        CaisseTamatave = Caisse.objects.all()
        if form.is_valid():
            form.save()
            soldeNow = solde.soldeInitial
            for caisse in CaisseTamatave:
                soldeNow = soldeNow + caisse.recette - caisse.depense

            solde.soldeActuel = soldeNow
            solde.save()
            messages.success(request,'success')
            return HttpResponseRedirect('/caisseTamatave/')
        else:
            messages.error(request,'error')
    else:
        form = SoldeForm(instance=solde)
    return render(request,'caisseTamatave/refSolde.html',{'form': form,'pageTitle':pageTitle})

def createCaisseTamatave(request):
    pageTitle = "Caisse Tamatave"
    subtitle = "Nouvelle enregistrement"
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'create')
            i = Solde.objects.latest('id')
            refSoldeTamatave(request,pk=i.pk)
        return HttpResponseRedirect('/caisseTamatave/')
    else:
        form = CaisseForm()
    return render(request,'caisseTamatave/edit.html',{'form':form,'pageTitle':pageTitle,'subtitle':subtitle})

def editCaisseTamatave(request,pk=None):
    pageTitle = "Caisse Tamatave"
    subtitle = "Edition"
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES,instance=caisse)

        if form.is_valid():
            form.save()
            messages.success(request,'success')
            i = Solde.objects.latest('id')
            refSoldeTamatave(request,pk=i.pk)
        return HttpResponseRedirect('/caisseTamatave/')

    else:
        form = CaisseForm(instance=caisse)
    return render(request,'caisseTamatave/edit.html',{'form': form,'pageTitle':pageTitle,'subtitle':subtitle})

def deleteCaisseTamatave(request,pk=None):
    pageTitle = "Caisse Tamatave"
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        caisse.delete()
        messages.success(request,'delete')
        return HttpResponseRedirect('/caisseTamatave/')

    return render(request,'caisseTamatave/delete.html',{'caisse':caisse,'pageTitle':pageTitle})
