from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from operation.models import Operation
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.db.models import Max

from accounts.views import *
# from accounts.urls import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_only, unauthenticated_user, allowed_users
from facture.models import BLMoto, FactureMoto
from moto.models import Moto
import datetime


# Create your views here.

@login_required(login_url='loginPage')
@admin_only
def home(request):
    topbar(request)
    pageTitle = "MTZ Admin"
    return render(request, 'base/home.html', {'pageTitle': pageTitle})


def main(request):
    return render(request, 'base/main.html')


def topbar(request):
    if request.is_ajax and request.method == 'GET':
        # ExportateurName = request.GET.get("ExportateurName",None)
        # print("ExportateurName = ",ExportateurName)
        # ExportateurIdBSC = Exportateur.objects.get(nom=ExportateurName).ID_BSC
        # print("ExportateurIdBSC = ",ExportateurIdBSC)
        operations = Operation.objects.all()
        notification = []
        counter = 0
        # numFactureLast = FactureMoto.objects.last().Num_Facture
        numFactureLast = Moto.objects.aggregate(Max('num_sur_facture'))[
            "num_sur_facture__max"]
        numBLlast = Moto.objects.aggregate(
            Max('num_BL'))["num_BL__max"]
        try:
            idMotoLast = str(Moto.objects.last().ID_Moto)
        except:
            idMotoLast = ""
        saved = int(idMotoLast)
        stock = saved
        for id in range(1, saved):
            if Moto.objects.get(id=id).num_sur_facture is not None or Moto.objects.get(id=id).num_BL is not None:
                stock = stock - 1
                # print("stock = ",stock)

        for op in operations:
            if not op.Prep_Full:
                notification.append(op.Reference_Reception)
                counter = counter + 1
        return JsonResponse(
            {"notification": notification, 'counter': counter, 'numFactureLast': numFactureLast, 'numBLlast': numBLlast,
             'idMotoLast': idMotoLast, 'stock': stock}, status=200)
    elif request.method == 'GET':
        test = "python test"
        return {'test': test}
