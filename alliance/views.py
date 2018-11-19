from django.shortcuts import render, redirect
from .models import Alliance
import mainPage.models
# Create your views here.


def show_your_alliance(request):
    user = request.user
    profil = mainPage.models.Profile.objects.get(user=user)
    if profil.alliance is not None:
        alliance = Alliance.objects.get(id=profil.user.id)
        return render(request, 'indexAlliance.html', {'alliance': alliance})
    else:
        alliances = Alliance.objects.all()
        return redirect('listOfAlliances/')


def alliance_list_page(request):
    alliances = Alliance.objects.all()
    return render(request, 'allianceList.html', {'alliances': alliances})


def alliance_detail_page(request, idOfAlliance):
    alliance = Alliance.objects.get(id=idOfAlliance)
    return render(request, 'allianceDetail.html', {'alliance': alliance})
