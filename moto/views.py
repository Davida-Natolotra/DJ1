from django.shortcuts import render, get_object_or_404
from moto.models import Moto
from moto.form import MotoForm, MotoFormCom
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.contrib import messages
from myapp.views import detail
from django.http.response import JsonResponse, HttpResponseRedirect
from facture.models import BLMoto, FactureMoto
import datetime


# Create your views here.

def index(request):
    motos = Moto.objects.all()
    count = len(motos)
    lastID = Moto.objects.last().ID_Moto
    pageTitle = "Moto"
    lastFacture = FactureMoto.objects.last().Num_Facture
    lastBL = BLMoto.objects.last().Num_BL
    return render(request, 'moto/index.html',
                  {'motos': motos, 'count': count, 'pageTitle': pageTitle, 'lastID': lastID, 'lastFacture': lastFacture,
                   'lastBL': lastBL})


def createMoto(request):
    pageTitle = "Moto"
    if request.method == 'POST':
        form = MotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'create')
            lastmoto = Moto.objects.last()
            print("pk = ", lastmoto.pk)
            return redirect('editMoto', pk=lastmoto.pk)
        else:
            messages.error(request, 'error')
    else:
        form = MotoForm()
        
    return render(request, 'moto/create.html', {'form': form, 'pageTitle': pageTitle})


def archiveMoto(request):
    if request.is_ajax and request.method == 'GET':
        id = request.GET.get("id", None)
        print("id = ", id)
        moto = get_object_or_404(Moto, pk=id)
        print("moto = ", moto)
        moto.archive = True
        moto.save()
        print("saved")
        # pageTitle = "Moto n°"+str(id)
        messages.success(request, "success")
        return JsonResponse({'archiveOK': 'archiveOK'}, status=200)
        # moto = get_object_or_404(Moto, pk=id)
        # form = MotoForm(request.POST, request.FILES, instance=moto)
        # return render(request, 'moto/detail.html', {'form': form, 'pageTitle': pageTitle})


def editMoto(request, pk=None):
    print("Edit moto")
    moto = get_object_or_404(Moto, pk=pk)
    id = moto.ID_Moto
    pk = moto.pk
    pageTitle = "Moto n°" + str(id)
    if request.method == 'POST':
        form = MotoForm(request.POST, request.FILES, instance=moto)

        if form.is_valid():
            form.save()
            messages.success(request, 'success')
        else:
            messages.error(request, 'error')
    else:
        form = MotoForm(instance=moto)

    return render(request, 'moto/edit.html', {'form': form, 'pageTitle': pageTitle, 'id': id, 'pk': pk})


def detailsMoto(request, pk=None):
    print("Edit moto")
    moto = get_object_or_404(Moto, pk=pk)
    id = moto.ID_Moto
    pageTitle = "Moto n°" + str(id)

    form = MotoForm(instance=moto)

    return render(request, 'moto/detail.html', {'form': form, 'pageTitle': pageTitle})


def deleteMoto(request, pk=None):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        moto.delete()
        messages.success(request, 'delete')
        return HttpResponseRedirect('/moto/')

    return render(request, 'moto/delete.html', {'moto': moto})


def chart(request):
    if request.is_ajax and request.method == 'GET':
        chart2 = request.GET.get("chart2", None)
        # print (chart2)
        if chart2 is not None:
            year = request.GET.get("yearChange", None)
            year = int(year)
            volana = 1
            andro = 1
        else:
            datehebdo = request.GET.get("datehebdo", None).split("-")
            dateMensuel = request.GET.get("dateMensuel", None).split("-")
            scopeChange = request.GET.get("scopeChange", None)
            year = int(datehebdo[0])
            volana = int(datehebdo[1])
            andro = int(datehebdo[2])

            # print("year = ", year)

            if scopeChange == "hebdomadaire":
                volana = int(datehebdo[1])
                andro = int(datehebdo[2])
            elif scopeChange == "mensuel":
                year = int(dateMensuel[0])
                volana = int(dateMensuel[1])
                andro = 1
        datamonth = {}
        data = {}
        monthday = {}
        datamonthname = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre',
                         'Octobre', 'Novembre', 'Decembre']
        mois = {}
        for i in range(12):
            mois[i + 1] = datamonthname[i]

        for month in range(1, 13, 1):
            counterMonth = 0
            counterDay = 0
            if month == 2:
                if year % 4 == 0:
                    datemax = 30
                else:
                    datemax = 29
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                datemax = 32
            elif month in [4, 6, 9, 11]:
                datemax = 31
            monthday[month] = datemax - 1
            for date in range(1, datemax, 1):
                formatDate = datetime.date(year, month, date)
                data[formatDate] = Moto.objects.filter(
                    date_vente=formatDate).count()
                counterDay = counterDay + Moto.objects.filter(date_vente=formatDate).count()
            counterMonth = counterMonth + counterDay
            datamonth[month] = counterMonth
            # print("datamonth = ",datamonth)
        datamonthnumber = {}
        for i in range(12):
            datamonthnumber[datamonthname[i]] = datamonth[i + 1]

        isambolana = {}
        for j in range(1, monthday[volana] + 1, 1):
            isambolana[j] = data[datetime.date(year, volana, j)]

        datatrimestre = {}
        trimestrename = ["Janvier-Fevrier-Mars", "Avril-Mai-Juin", "Juillet-Aout-Septembre",
                         "Octobre-Novembre-Decembre"]
        for trimestre in [1, 2, 3, 4]:
            if trimestre == 1:
                trimestrecount = 0
                for month in [1, 2, 3]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestrename[trimestre - 1]] = trimestrecount
            if trimestre == 2:
                trimestrecount = 0
                for month in [4, 5, 6]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestrename[trimestre - 1]] = trimestrecount
            if trimestre == 3:
                trimestrecount = 0
                for month in [7, 8, 9]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestrename[trimestre - 1]] = trimestrecount
            if trimestre == 4:
                trimestrecount = 0
                for month in [10, 11, 12]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestrename[trimestre - 1]] = trimestrecount

        # print("datatrimestre = ",datatrimestre)

        datasemestre = {}
        semestrename = ["Janvier-Juin", "Juillet-Decembre"]
        for semestre in [1, 2]:
            if semestre == 1:
                semestrecount = 0
                for month in [1, 2, 3, 4, 5, 6]:
                    semestrecount = semestrecount + datamonth[month]
                datasemestre[semestrename[semestre - 1]] = semestrecount
            if semestre == 2:
                semestrecount = 0
                for month in [7, 8, 9, 10, 11, 12]:
                    semestrecount = semestrecount + datamonth[month]
                datasemestre[semestrename[semestre - 1]] = semestrecount

        datayear = {}
        yearcount = 0
        for month in range(1, 13, 1):
            yearcount = yearcount + datamonth[month]
        datayear[year] = yearcount
        # print("data = ",data)
        # print("data androany",data[datetime.date(year,volana,andro)])
        dataweek = {}
        datestart = datetime.date(year, volana, andro)
        if datestart.day + 7 > monthday[volana]:
            dateDelta = monthday[volana] - datestart.day
            # print(f"Mihoatra {dateDelta} andro")
            for jour in range(andro, monthday[volana] + 1, 1):
                dataweek[str(jour) + " " + str(mois[volana])] = data[datetime.date(year, volana, jour)]
            for jour in range(1, 7 - dateDelta, 1):
                if volana == 12:
                    dataweek[str(jour) + " " + str(mois[1])] = data[datetime.date(year, 1, jour)]
                else:
                    dataweek[str(jour) + " " + str(mois[volana + 1])] = data[datetime.date(year, volana + 1, jour)]

        else:
            for jour in range(andro, andro + 7, 1):
                # print("jour:",jour)
                dataweek[str(jour) + " " + str(mois[volana])] = data[datetime.date(year, volana, jour)]
        # print("dataweek= ",dataweek)
        # print("dataweek.keys() = ",list(dataweek.keys()))
        return JsonResponse({
            "date": list(dataweek.keys()),
            "data": list(dataweek.values()),
            "jourMois": list(isambolana.keys()),
            "nombMois": list(isambolana.values()),
            "month": list(datamonthnumber.keys()),
            "datamonth": list(datamonthnumber.values()),
            "trimestre": list(datatrimestre.keys()),
            "datatrimestre": list(datatrimestre.values()),
            'semestre': list(datasemestre.keys()),
            "datasemestre": list(datasemestre.values())
        })

    elif request.method == 'POST':
        test = "python test"
        return {'test': test}
