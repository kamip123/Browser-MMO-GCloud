from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import cityMap.models
from django.http import JsonResponse
from mainPage.models import Profile
from django.contrib.auth.models import User
from .models import Attack
# Create your views here.


@login_required(login_url='../../../../../../../')
def main_page_map(request):
    city_list = cityMap.models.CityOwned.objects.all()
    attacks = Attack.objects.all()
    return render(request, 'indexWorldMap.html', {'city_list': city_list, 'attacks': attacks})


@login_required(login_url='../../../../../../../')
def return_citys_list(request):
    data = cityMap.models.CityOwned.objects.all().values()
    data = list(data)
    return JsonResponse(data, safe=False)


@login_required(login_url='../../../../../../../')
def return_citys_list_test(request):
    return render(request, 'test.html')


@login_required(login_url='../../../../../../../')
def city_detail_info(request, id_of_city):
    city = cityMap.models.CityOwned.objects.get(id=id_of_city)
    return render(request, 'cityDetailInfo.html', {'city': city})


@login_required(login_url='../../../../../../../')
def city_owner_detail_info(request, id_of_city, id_of_user):
    user = User.objects.get(id=id_of_user)
    citys = cityMap.models.CityOwned.objects.filter(city_owner=user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetailInfo.html', {'user': user, 'profil': profil, 'citys': citys})
