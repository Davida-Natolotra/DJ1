from moto.models import Moto
import datetime

def chart(year):
    for year in range(2020, 2025):
        datamonth = {}
        data = {}
        for month in range(1, 13, 1):
            counterMonth = 0
            counterDay = 0
            if month == 2:
                if year == 2020 or year == 2024:
                    datemax = 30
                else:
                    datemax = 29
            elif month in [1,3,5,7,8,10,12]:
                datemax = 32
            elif month in [4,6,9,11]:
                datemax = 31
            print('month = ', month)
            print("datemax = ", datemax-1)
            for date in range(1, datemax, 1):
                formatDate = datetime.date(year, month, date)
                data[formatDate] = Moto.objects.filter(date_vente=formatDate).count()
                counterDay = counterDay + Moto.objects.filter(date_vente=formatDate).count()
                counterMonth = counterMonth + counterDay
                datamonth[month] = counterMonth
            datamonthname = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
            datamonthnumber = {}
            for i in range(12):
                datamonthnumber[datamonthname[i]] = datamonth[i+1]
        datatrimestre = {}
        for trimestre in [1,2,3,4]:
            if trimestre == 1:
                trimestrecount = 0
                for month in [1,2,3]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestre] = trimestrecount
            if trimestre == 2:
                trimestrecount = 0
                for month in [4,5,6]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestre] = trimestrecount
            if trimestre == 3:
                trimestrecount = 0
                for month in [7,8,9]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestre] = trimestrecount
            if trimestre == 4:
                trimestrecount = 0
                for month in [10,11,12]:
                    trimestrecount = trimestrecount + datamonth[month]
                datatrimestre[trimestre] = trimestrecount
        datasemestre = {}
        for semestre in [1,2]:
            if semestre == 1:
                semestrecount = 0
                for month in [1,2,3,4,5,6]:
                    semestrecount = semestrecount + datamonth[month]
                datasemestre[semestre] = semestrecount
            if semestre == 2:
                semestrecount = 0
                for month in [7,8,9,10,11,12]:
                    semestrecount = semestrecount + datamonth[month]
                datasemestre[semestre] = semestrecount
        datayear = {}
        yearcount = 0
        for month in range(1,13,1):
            yearcount = yearcount + datamonth[month]
        datayear[year] = yearcount