from django.shortcuts import render, get_object_or_404
from .form import CaisseForm
from .models import Caisse, Solde
from .soldeForm import SoldeForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.
def indexTana(request):
    caisseTanas = Caisse.objects.all()
    solde = Solde.objects.all()
    return render(request,'caisseTana/index.html',{'caisseTanas':caisseTanas,'solde':solde})

def refSoldeTana(request,pk=None):
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
    return render(request,'caisseTana/refSolde.html',{'form': form})

def createCaisseTana(request):
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            i = Solde.objects.latest('id')
            refSoldeTana(request,pk=i.pk)
        return HttpResponseRedirect('/caisseTana/')
    else:
        form = CaisseForm()
    return render(request,'caisseTana/edit.html',{'form':form})

def editCaisseTana(request,pk=None):
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        form = CaisseForm(request.POST,request.FILES,instance=caisse)

        if form.is_valid():
            form.save()
            i = Solde.objects.latest('id')
            refSoldeTana(request,pk=i.pk)
        return HttpResponseRedirect('/caisseTana/')
        
    else:
        form = CaisseForm(instance=caisse)
    return render(request,'caisseTana/edit.html',{'form': form})

def deleteCaisseTana(request,pk=None):
    caisse = get_object_or_404(Caisse, pk=pk)
    if request.method == 'POST':
        caisse.delete()
        return HttpResponseRedirect('/caisseTana/')

    return render(request,'caisseTana/delete.html',{'caisse':caisse})
