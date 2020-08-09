from django.shortcuts import render, get_object_or_404
from moto.models import Moto
from django.http import HttpResponseRedirect
from moto.form import MotoForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    motos = Moto.objects.all()
    return render(request,'moto/index.html',{'motos':motos})

def createMoto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = MotoForm()
    return render(request,'moto/edit.html',{'form':form})

def editMoto(request,pk=None):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        form = MotoForm(request.POST,request.FILES,instance=moto)

        if form.is_valid():
            form.save()

    else:
        form = MotoForm(instance=moto)
    return render(request,'moto/edit.html',{'form': form})

def deleteMoto(request,pk=None):
    moto = get_object_or_404(Moto,pk=pk)
    if request.method == 'POST':
        moto.delete()
        return HttpResponseRedirect('/moto/')

    return render(request,'moto/delete.html',{'moto':moto})
