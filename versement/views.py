from django.shortcuts import render, get_object_or_404
from .form import VersementForm
from .models import Versement
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.
def indexVersement(request):
    versements = Versement.objects.all()
    pageTitle = "Versement"
    return render(request, 'versement/index.html', {'versements': versements, 'pageTitle': pageTitle})

def createVersement(request):
    pagetitle = "Versement"
    subtitle = "Nouvelle enregistrement"
    if request.method == 'POST':
        form = VersementForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = VersementForm()
    return render(request,'versement/edit.html',{'form':form,'pageTitle':pagetitle,'subtitle':subtitle})

def editVersement(request,pk=None):
    pageTitle = "Versement"
    subtitle = "Edition"
    versement = get_object_or_404(Versement, pk=pk)
    if request.method == 'POST':
        form = VersementForm(request.POST,request.FILES,instance=versement)

        if form.is_valid():
            form.save()

    else:
        form = VersementForm(instance=versement)
    return render(request,'versement/edit.html',{'form': form,'pageTitle':pageTitle,'subtitle':subtitle})

def deleteVersement(request,pk=None):
    versement = get_object_or_404(Versement,pk=pk)
    if request.method == 'POST':
        versement.delete()
        return HttpResponseRedirect('/versement/')
    return render(request,'versement/delete.html',{'versement':versement})
