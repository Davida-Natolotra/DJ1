from django.shortcuts import render, get_object_or_404
from .form import CaisseForm
from .models import Caisse, Solde
from .soldeForm import SoldeForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def indexTana(request):
    caisseTanas = Caisse.objects.all()
    solde = Solde.objects.all()
    pageTitle = "Caisse Tana"
    return render(request,'caisseTana/index.html',{'caisseTanas':caisseTanas,'solde':solde,'pageTitle':pageTitle})

def refSoldeTana(request,pk=None):
    pageTitle = "Caisse Tana"
    solde = get_object_or_404(Solde, pk=pk)
    if request.method == 'POST':
        form = SoldeForm(request.POST,instance=solde)

        CaisseTana = Caisse.objects.all()
        if form.is_valid():
            form.save()
            soldeNow = solde.soldeInitial
            for caisse in CaisseTana:
                soldeNow = soldeNow + caisse.recette - caisse.depense

            solde.soldeActuel = soldeNow
            solde.save()

        return HttpResponseRedirect('/caisseTana/')
    else:
        form = SoldeForm(instance=solde)
    return render(request,'caisseTana/refSolde.html',{'form': form,'pageTitle':pageTitle})

def createCaisseTana(request):
    pageTitle = "Caisse Tana"
    subtitle = "Nouvelle enregistrement"
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'create')
            i = Solde.objects.latest('id')
            refSoldeTana(request,pk=i.pk)
        return HttpResponseRedirect('/caisseTana/')
    else:
        form = CaisseForm()
    return render(request,'caisseTana/edit.html',{'form':form,'pageTitle':pageTitle,'subtitle':subtitle})

def editCaisseTana(request,pk=None):
    pageTitle = "Caisse Tana"
    subtitle = "Edition"
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES,instance=caisse)

        if form.is_valid():
            form.save()
            messages.success(request,'success')
            i = Solde.objects.latest('id')
            refSoldeTana(request,pk=i.pk)
        else:
            message = "error"
        return HttpResponseRedirect('/caisseTana/')

    else:
        message = ""
        form = CaisseForm(instance=caisse)
    return render(request,'caisseTana/edit.html',{'form': form,'pageTitle':pageTitle,'subtitle':subtitle})

def deleteCaisseTana(request,pk=None):
    pageTitle = "Caisse Tana"
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        caisse.delete()
        messages.info(request,'delete')
        return HttpResponseRedirect('/caisseTana/')

    return render(request,'caisseTana/delete.html',{'caisse':caisse,'pageTitle':pageTitle})
