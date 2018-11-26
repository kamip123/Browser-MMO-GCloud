from django.shortcuts import render, redirect
from .models import CityOwned
from mainPage.models import Server, CityPositions
from .forms import CityOwnedForm
import random
# Create your views here.


def main_page_city_list(request):
    user = request.user
    cityList = CityOwned.objects.all().filter(cityOwner=user.id)
    return render(request, 'indexCityList.html', {'cityList': cityList})


def main_page_city_id(request, idOfCity):
    brakMiasta = 0
    user = request.user
    city = CityOwned.objects.get(cityOwner=user.id, id=idOfCity)
    return render(request, 'indexCityMap.html', {'brakMiasta': brakMiasta, 'city': city})


def town_hall_city_id(request, idOfCity):
    return render(request, 'townhall.html', {'idOfCity': idOfCity})


def barracks_city_id(request, idOfCity):
    return render(request, 'barracks.html', {'idOfCity': idOfCity})


def main_page_city(request):
    user = request.user
    if request.method == 'POST':
        form = CityOwnedForm(request.POST)
        try:
            city = CityOwned.objects.get(cityOwner=user.id)
        except CityOwned.DoesNotExist:
            if form.is_valid():

                city = form.save(commit=False)
                city.cityOwner = user

                server = Server.objects.get(id=1)
                city.pozX = server.nextVillageX
                city.pozY = server.nextVillageY
                server.nextVillageId = server.nextVillageId + 1
                server.save()
                nextCityPos = CityPositions.objects.get(id=server.nextVillageId+100)
                server.update_village_pos(nextCityPos.villageX, nextCityPos.villageY)

                city.ratusz = 2
                city.koszary = 2
                city.drogi = 1
                city.kopalnia = 1
                city.elektrownia = 1
                city.farmy = 1
                city.is_Capital = True
                city.save()
                brakMiasta = 0
                return redirect('cityList/')
            else:
                city = CityOwned.objects.filter(cityOwner=user.id)
                brakMiasta = 1
                return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta, 'form': form})

    elif user.is_authenticated:
        try:
            city = CityOwned.objects.get(cityOwner=user.id, is_capital=True)
        except CityOwned.DoesNotExist:
            brakMiasta = 1
            form = CityOwnedForm()
            return render(request, 'indexCityMap.html', {'brakMiasta': brakMiasta, 'form': form})

        city = CityOwned.objects.get(cityOwner=user.id, is_capital=True)
        brakMiasta = 0

        #city.updateBuildings()
        #city.save()
        #if city.ratuszBudowaTrwa != 1:
        #    city.rozbudujRatusz()
        #    city.save()
        try:
            rozbudowaRatuszaTimestamp = city.ratuszBudowa.timestamp()
        except:
            return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta})

        return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta, 'rozbudowaRatuszaTimestamp': rozbudowaRatuszaTimestamp})
    else:
        return redirect('../')


def colonize_new_city(request):
    have_enought_resources = 1
    if have_enought_resources == 1:
        city = CityOwned(cityName="New City")
        city.cityOwner = request.user

        server = Server.objects.get(id=1)
        city.pozX = server.nextVillageX
        city.pozY = server.nextVillageY
        server.nextVillageId = server.nextVillageId + 1
        server.save()
        nextCityPos = CityPositions.objects.get(id=server.nextVillageId + 100)
        server.update_village_pos(nextCityPos.villageX, nextCityPos.villageY)
        server.save()

        city.ratusz = 2
        city.koszary = 2
        city.drogi = 1
        city.kopalnia = 1
        city.elektrownia = 1
        city.farmy = 1
        city.is_Capital = False
        city.save()
        return redirect('../cityList/')
