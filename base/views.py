from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from operation.models import Operation
# Create your views here.
def home(request):
    topbar(request)
    return render(request, 'base/home.html')

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
        for op in operations:
            if not op.Prep_Full:
                notification.append(op.Reference_Reception)
                counter = counter +1
        return JsonResponse({"notification":notification,'counter':counter},status=200)
    elif request.method == 'GET':
        test = "python test"
        return {'test':test}
