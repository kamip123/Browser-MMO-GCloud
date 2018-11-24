from django.shortcuts import render
import cityMap.models
from django.core import serializers
from django.http import JsonResponse
from mainPage.models import Profile
from django.core.serializers import serialize
from django.contrib.auth.models import User
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


def city_detail_info(request, idOfCity):
    city = cityMap.models.CityOwned.objects.get(id=idOfCity)
    return render(request, 'cityDetailInfo.html', {'city': city})


def city_owner_detail_info(request, idOfCity, idOfUser):
    user = User.objects.get(id=idOfUser)
    citys = cityMap.models.CityOwned.objects.filter(cityOwner=user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetailInfo.html', {'user': user, 'profil': profil, 'citys': citys})
