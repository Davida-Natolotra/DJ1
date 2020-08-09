from django.shortcuts import render, get_object_or_404
from myapp.models import Flower
from django.http import HttpResponseRedirect
from .form import MyForm
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    flowers = Flower.objects.all()
    return render(request,'myapp/index.html',{'flowers':flowers})

def detail(request,id=None):
    flower = get_object_or_404(Flower,id=id)
    return render(request,'myapp/detail.html',{'flower':flower})

def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myapp')
    else:
        form = MyForm()
    return render(request,'myapp/edit.html',{'form':form})

def edit(request,pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES,instance=flower)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    return render(request,'myapp/edit.html',{'form': form})

def delete(request,pk=None):
    flower = get_object_or_404(Flower,pk=pk)
    if request.method == 'POST':
        flower.delete()
        return HttpResponseRedirect('/myapp')

    return render(request,'myapp/delete.html',{'flower':flower})
