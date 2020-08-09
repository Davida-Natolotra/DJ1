from django.shortcuts import render, get_object_or_404
from importateur.models import Importateur
from django.http import HttpResponseRedirect
from importateur.form import ImportateurForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def indexImportateur(request):
    importateurs = Importateur.objects.all()
    return render(request,'importateur/index.html',{'importateurs':importateurs})

def createImportateur(request):
    if request.method == 'POST':
        form = ImportateurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/importateur')
    else:
        form = ImportateurForm()
    return render(request,'importateur/edit.html',{'form':form})

def editImportateur(request,pk=None):
    importateur = get_object_or_404(Importateur, pk=pk)
    if request.method == 'POST':
        form = ImportateurForm(request.POST,request.FILES,instance=importateur)

        if form.is_valid():
            form.save()

    else:
        form = ImportateurForm(instance=importateur)
    return render(request,'importateur/edit.html',{'form': form})

def deleteImportateur(request,pk=None):
    importateur = get_object_or_404(Importateur,pk=pk)
    if request.method == 'POST':
        importateur.delete()
        return HttpResponseRedirect('/importateur/')

    return render(request,'importateur/delete.html',{'importateur':importateur})
