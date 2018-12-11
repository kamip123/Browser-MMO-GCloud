from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainPage.views import main_page
from .models import Premium, Tranzakcja
from mainPage.models import Profile
from django.utils import timezone
# Create your views here.


@login_required(login_url=main_page)
def premium_page(request):
    premiumOptions = Premium.objects.get(id=1)
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=request.user)
        profile.is_premium = True
        profile.until_premium = timezone.now()
        #profile.until_premium = timezone.now() + timedelta(days = 30)
        profile.save()
        tranzakcja = Tranzakcja(buyer=user, type_of_premium=request.POST.get('typPremium', False))
        tranzakcja.save()

    return render(request, 'indexPremium.html', {'premiumOptions': premiumOptions})


@login_required(login_url=main_page)
def premium_platnosc(request):
    user = request.user
    return render(request, 'zaplac.html')


@login_required(login_url=main_page)
def premium_history(request):
    user = request.user
    tranzakcje = Tranzakcja.objects.all().filter(buyer=user)
    return render(request, 'platnosci.html', {'tranzakcje': tranzakcje})
