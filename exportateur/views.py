from django.shortcuts import render, get_object_or_404
from exportateur.models import Exportateur
from django.http import HttpResponseRedirect
from exportateur.form import ExportateurForm
from django.core.files.storage import FileSystemStorage

pageTitle = 'Exportateur'
# Create your views here.
def indexExportateur(request):
    exportateurs = Exportateur.objects.all()
    context = {
        'exportateurs':exportateurs,
        'pageTitle':pageTitle
        }
    return render(request,'exportateur/index.html',context)

def createExportateur(request):
    if request.method == 'POST':
        form = ExportateurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exportateur')
    else:
        form = ExportateurForm()
    return render(request,'exportateur/edit.html',{'form':form,'pageTitle':pageTitle})

def editExportateur(request,pk=None):
    exportateur = get_object_or_404(Exportateur, pk=pk)
    if request.method == 'POST':
        form = ExportateurForm(request.POST,request.FILES,instance=exportateur)

        if form.is_valid():
            form.save()

    else:
        form = ExportateurForm(instance=exportateur)
    return render(request,'exportateur/edit.html',{'form': form,'pageTitle':pageTitle})

def deleteExportateur(request,pk=None):
    exportateur = get_object_or_404(Exportateur,pk=pk)
    if request.method == 'POST':
        exportateur.delete()
        return HttpResponseRedirect('/exportateur/')

    return render(request,'exportateur/delete.html',{'exportateur':exportateur})
