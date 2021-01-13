from django.shortcuts import render, get_object_or_404
from importateur.models import Importateur
from django.http import HttpResponseRedirect
from importateur.form import ImportateurForm
from django.core.files.storage import FileSystemStorage

pageTitle = "Importateur"


# Create your views here.
def indexImportateur(request):
    importateurs = Importateur.objects.all()
    context = {
        'importateurs': importateurs,
        'pageTitle': pageTitle,
    }
    return render(request, 'importateur/index.html', context)


def createImportateur(request):
    if request.method == 'POST':
        form = ImportateurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/importateur')
    else:
        form = ImportateurForm()
    context = {
        'form': form,
        'pageTitle': pageTitle,
    }
    return render(request, 'importateur/edit.html', context)


def editImportateur(request, pk=None):
    importateur = get_object_or_404(Importateur, pk=pk)
    if request.method == 'POST':
        form = ImportateurForm(request.POST, request.FILES, instance=importateur)

        if form.is_valid():
            form.save()

    else:
        form = ImportateurForm(instance=importateur)
    context = {
        'form': form,
        'pageTitle': pageTitle,
               }
    return render(request, 'importateur/edit.html', context)


def deleteImportateur(request, pk=None):
    importateur = get_object_or_404(Importateur, pk=pk)
    if request.method == 'POST':
        importateur.delete()
        return HttpResponseRedirect('/importateur/')

    return render(request, 'importateur/delete.html', {'importateur': importateur})
