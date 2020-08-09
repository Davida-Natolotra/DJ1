from django.shortcuts import render, get_object_or_404
from compagnie.models import Compagnie
from django.http import HttpResponseRedirect
from compagnie.form import CompagnieForm

# Create your views here.
def indexCompagnie(request):
    compagnies = Compagnie.objects.all()
    return render(request,'compagnie/index.html',{'compagnies':compagnies})

def createCompagnie(request):
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compagnie')
    else:
        form = CompagnieForm()
    return render(request,'compagnie/edit.html',{'form':form})

def editCompagnie(request,pk=None):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    if request.method == 'POST':
        form = CompagnieForm(request.POST,instance=compagnie)
        if form.is_valid():
            form.save()

    else:
        form = CompagnieForm(instance=compagnie)
    return render(request,'compagnie/edit.html',{'form':form})

def deleteCompagnie(request,pk=None):
    compagnie = get_object_or_404(Compagnie,pk=pk)
    if request.method == 'POST':
        compagnie.delete()
        return HttpResponseRedirect('/compagnie/')

    return render(request,'compagnie/delete.html',{'compagnie':compagnie})
