from django.shortcuts import render
import cityMap.models
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.


def main_page_map(request):
    cityList = cityMap.models.CityOwned.objects.all()
    return render(request, 'indexWorldMap.html', {'cityList': cityList})


def return_citys_list(request):
    data = cityMap.models.CityOwned.objects.all().values()
    data = list(data)
    return JsonResponse(data, safe=False)


def return_citys_list_test(request):
    return render(request, 'test.html')
