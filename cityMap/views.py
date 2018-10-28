from django.shortcuts import render
from .models import CityOwned
from .forms import CityOwnedForm

# Create your views here.


def main_page_city(request):
    user = request.user
    if request.method == 'POST':
        form = CityOwnedForm(request.POST)
        if form.is_valid():

            city = form.save(commit=False)
            city.cityOwner = user
            city.pozX = 1
            city.pozY = 1
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
        city = CityOwned.objects.get(cityOwner=user.id)
        brakMiasta = 0
        if not city:
            brakMiasta = 1
            form = CityOwnedForm()
            return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta, 'form': form})
        #city.updateBuildings()
        #city.save()
        #if city.ratuszBudowaTrwa != 1:
        #    city.rozbudujRatusz()
        #    city.save()

        rozbudowaRatuszaTimestamp = city.ratuszBudowa.timestamp()
        return render(request, 'indexCityMap.html', {'city': city, 'brakMiasta': brakMiasta, 'rozbudowaRatuszaTimestamp': rozbudowaRatuszaTimestamp})

    return render(request, 'indexCityMap.html')
