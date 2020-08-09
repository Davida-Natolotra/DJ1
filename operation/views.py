from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage

from operation.dedouannementform import dedouannementForm
from operation.models import Operation
from operation.forms import preparationForm
from operation.receptionForm import ReceptionForm
from exportateur.models import Exportateur
from importateur.models import Importateur
from compagnie.models import Compagnie

# Create your views here.
def indexOperation(request):
    operations = Operation.objects.all()
    return render(request,'operation/index.html',{'operations':operations})

def createReception(request):
    if request.method == 'POST':
        form = ReceptionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/operation/')
    else:
        form = ReceptionForm()
    return render(request,'operation/editReception.html',{'form':form})

def editReception(request,pk=None):
    operation = get_object_or_404(Operation,pk=pk)
    if request.method == 'POST':
        form = ReceptionForm(request.POST,request.FILES,instance=operation)
        if form.is_valid():
            form.save()

    else:
        form = ReceptionForm(instance=operation)
    return render(request,'operation/editReception.html',{'form':form})

def deleteOperation(request,pk=None):
    operation = get_object_or_404(Operation,pk=pk)
    if request.method == 'POST':
        operation.delete()
        return HttpResponseRedirect('/operation/')

    return render(request,'operation/delete.html',{'operation':operation})

def editPreparation(request,pk=None):
    operation = get_object_or_404(Operation,pk=pk)
    if request.method == 'POST':
        form = preparationForm(request.POST,request.FILES,instance=operation)
        if form.is_valid():
            form.save()

    else:
        form = preparationForm(instance=operation)
    return render(request,'operation/editPreparation.html',{'form':form})

def editDedouannement(request,pk=None):
    operation = get_object_or_404(Operation,pk=pk)
    if request.method == 'POST':
        form = dedouannementForm(request.POST,request.FILES,instance=operation)
        if form.is_valid():
            form.save()

    else:
        form = dedouannementForm(instance=operation)
    return render(request,'operation/editDedouannement.html',{'form':form})


def ExportateurData(request):
    if request.is_ajax and request.method == 'GET':
        ExportateurName = request.GET.get("ExportateurName",None)
        print("ExportateurName = ",ExportateurName)
        ExportateurIdBSC = Exportateur.objects.get(nom=ExportateurName).ID_BSC
        print("ExportateurIdBSC = ",ExportateurIdBSC)
        return JsonResponse({"ExportateurIdBSC":ExportateurIdBSC},status=200)

def ImportateurData(request):
    if request.is_ajax and request.method == 'GET':
        ImportateurName = request.GET.get("ImportateurName",None)
        print("ImportateurName = ",ImportateurName)
        ImportateurIdBSC = Importateur.objects.get(nom=ImportateurName).ID_BSC
        DomBanque = Importateur.objects.get(nom=ImportateurName).banque
        print("ImportateurIdBSC = ",ImportateurIdBSC)
        return JsonResponse({"ImportateurIdBSC":ImportateurIdBSC,'DomBanque':DomBanque},status=200)

def CompanyData(request):
    if request.is_ajax and request.method == 'GET':
        CompanyName = request.GET.get("CompanyName",None)
        print("CompanyName = ",CompanyName)
        adresseTana = Compagnie.objects.get(nomCompagnie=CompanyName).adresseTana
        print("adresseTana = ",adresseTana)
        adresseTamatave = Compagnie.objects.get(nomCompagnie=CompanyName).adresseTamatave
        print("adresseTamatave = ",adresseTamatave)
        email1 = Compagnie.objects.get(nomCompagnie=CompanyName).email1
        email2 = Compagnie.objects.get(nomCompagnie=CompanyName).email2
        email3 = Compagnie.objects.get(nomCompagnie=CompanyName).email3
        contact = Compagnie.objects.get(nomCompagnie=CompanyName).contact

        return JsonResponse({"adresseTana":adresseTana,'adresseTamatave':adresseTamatave,'email1':email1,'email2':email2,'email3':email3,'contact':contact},status=200)
