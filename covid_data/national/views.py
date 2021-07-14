from django.shortcuts import render
from django.http import HttpResponse
from tasks import getNationalData, setNationalData, setStateData, setPastStateData
from national.models import Data as NationalData
# Create your views here.
class NationalDataView():
    pass

def index(request):
    if request.method == 'GET':
        all_national_data = NationalData.objects.all()
        if not all_national_data:
            setNationalData()
            all_national_data = NationalData.objects.all()
        print(all_national_data)
        return HttpResponse(all_national_data)