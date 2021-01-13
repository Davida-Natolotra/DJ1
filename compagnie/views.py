from django.shortcuts import render, get_object_or_404
from compagnie.models import Compagnie
from django.http import HttpResponseRedirect
from compagnie.form import CompagnieForm

pageTitle = 'Compagnie'
# Create your views here.
def indexCompagnie(request):
    compagnies = Compagnie.objects.all()
    context = {
        'compagnies':compagnies,
        'pageTitle': pageTitle,
        }
    return render(request,'compagnie/index.html',context)

def createCompagnie(request):
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compagnie')
    else:
        form = CompagnieForm()
    context = {
        'form':form,
        'pageTitle':pageTitle
        }
    return render(request,'compagnie/edit.html',context)

def editCompagnie(request,pk=None):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    if request.method == 'POST':
        form = CompagnieForm(request.POST,instance=compagnie)
        if form.is_valid():
            form.save()

    else:
        form = CompagnieForm(instance=compagnie)
    context = {
        'form':form,
        'pageTitle':pageTitle
        }    
    return render(request,'compagnie/edit.html',context)

def deleteCompagnie(request,pk=None):
    compagnie = get_object_or_404(Compagnie,pk=pk)
    if request.method == 'POST':
        compagnie.delete()
        return HttpResponseRedirect('/compagnie/')

    return render(request,'compagnie/delete.html',{'compagnie':compagnie})
