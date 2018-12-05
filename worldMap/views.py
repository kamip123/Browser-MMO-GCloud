from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import cityMap.models
from mainPage.models import Profile
from django.contrib.auth.models import User
from .models import Attack
from cityMap.models import CityOwned
from rest_framework.utils import json
import math
from django.utils import timezone
# Create your views here.


@login_required(login_url='../../../../../../../')
def main_page_map(request):
    city_list = cityMap.models.CityOwned.objects.all()
    attacks = Attack.objects.all()
    return render(request, 'indexWorldMap.html', {'city_list': city_list, 'attacks': attacks})


@login_required(login_url='../../../../../../../')
def city_detail_info(request, id_of_city):
    city = cityMap.models.CityOwned.objects.get(id=id_of_city)
    return render(request, 'cityDetailInfo.html', {'city': city})


@login_required(login_url='../../../../../../../')
def city_attack(request, id_of_city):
    attack_succesfull = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        attack_correct = data['attack_correct']
        if attack_correct == 1:
            attacker_city = CityOwned.objects.get(id=data['attacking_city'])
            defender_city = CityOwned.objects.get(id=id_of_city)
            attack = Attack(attacker=attacker_city,
                            defender=defender_city, infantry=data['infantry'],
                            hinfantry=data['hinfantry'], planes=data['planes'], ltanks=data['ltanks'],
                            htanks=data['htanks'], motorized=data['motorized'])
            distance_between_citys = math.sqrt((defender_city.pos_x - attacker_city.pos_x)**2 + (defender_city.pos_y - attacker_city.pos_y)**2)
            attack.arrive = timezone.now() + timezone.timedelta(seconds=int(distance_between_citys))
            attack.save()
            attack_succesfull = 1
            return render(request, 'attacks.html', {'id_of_city': id_of_city, 'attack_succesfull': attack_succesfull})
        return render(request, 'attacks.html', {'id_of_city': id_of_city, 'attack_succesfull': attack_succesfull})
    return render(request, 'attacks.html', {'id_of_city': id_of_city, 'attack_succesfull': attack_succesfull})


@login_required(login_url='../../../../../../../')
def city_owner_detail_info(request, id_of_city, id_of_user):
    user = User.objects.get(id=id_of_user)
    citys = cityMap.models.CityOwned.objects.filter(city_owner=user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetailInfo.html', {'user': user, 'profil': profil, 'citys': citys})
