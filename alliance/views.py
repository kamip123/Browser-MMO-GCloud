from django.shortcuts import render, redirect
from .models import Alliance
from mainPage.models import Profile
from django.contrib.auth.models import User
# Create your views here.


def show_your_alliance(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.alliance is not None:
        alliance = Alliance.objects.get(id=profile.user.id)
        return render(request, 'indexAlliance.html', {'alliance': alliance})
    else:
        alliance = 1
        return render(request, 'indexAlliance.html', {'alliance': alliance})


def alliance_list_page(request):
    alliances = Alliance.objects.all()
    return render(request, 'allianceList.html', {'alliances': alliances})


def alliance_detail_page(request, id_of_alliance):
    alliance = Alliance.objects.get(id=id_of_alliance)
    return render(request, 'allianceDetail.html', {'alliance': alliance})


def user_detail_page(request, id_of_alliance, id_of_user):
    user = User.objects.get(id=id_of_user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetail.html', {'user': user, 'profil': profil})


def user_your_alliance_detail_page(request, id_of_user):
    user = User.objects.get(id=id_of_user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetail.html', {'user': user, 'profil': profil})
