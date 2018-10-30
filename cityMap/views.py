from django.shortcuts import render
from .models import CityOwned
from .forms import CityOwnedForm
import random
# Create your views here.


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
                city.pozX = random.randint(100, 400)
                city.pozY = random.randint(100, 400)
                city.ratusz = 2
                city.koszary = 2
                city.drogi = 1
                city.kopalnia = 1
                city.elektrownia = 1
                city.farmy = 1
                city.save()
                brakMiasta = 0
                return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta})
            else:
                city = CityOwned.objects.filter(cityOwner=user.id)
                brakMiasta = 1
                return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta, 'form': form})

    elif user.is_authenticated:
        try:
            city = CityOwned.objects.get(cityOwner=user.id)
        except CityOwned.DoesNotExist:
            brakMiasta = 1
            form = CityOwnedForm()
            return render(request, 'indexCityMap.html', {'brakMiasta': brakMiasta, 'form': form})

        city = CityOwned.objects.get(cityOwner=user.id)
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

    return render(request, 'indexCityMap.html')
