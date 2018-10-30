from django.shortcuts import render
import cityMap.models
from django.core.serializers import serialize
# Create your views here.


def main_page_map(request):
    cityList = cityMap.models.CityOwned.objects.all()
    return render(request, 'indexWorldMap.html', {'cityList': cityList})
