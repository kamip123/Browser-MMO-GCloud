from django.shortcuts import render
from .models import BattleRaport, AllianceInvite, HelpRaport, SpecialResourceRaport, TradeRaport

# Create your views here.

def raport_page(request):
    battleraports = BattleRaport.objects.filter(defender=request.user).order_by('created_date')
    alliancereports = AllianceInvite.objects.filter(receiver=request.user).order_by('created_date')
    helpraports = HelpRaport.objects.filter(receiver=request.user).order_by('created_date')
    specialresourceraports = SpecialResourceRaport.objects.filter(receiver=request.user).order_by('created_date')
    tradeeraports = TradeRaport.objects.filter(receiver=request.user).order_by('created_date')
    return render(request, 'indexRaports.html', {'battleraports': battleraports, 'alliancereports': alliancereports, 'helpraports': helpraports, 'specialresourceraports': specialresourceraports, 'tradeeraports': tradeeraports})


def raport_detail_page(request, idOfRaport, typeOfRaport):
    if typeOfRaport == 0:
        raport = BattleRaport.objects.get(id=idOfRaport)
    elif typeOfRaport == 1:
        raport = AllianceInvite.objects.get(id=idOfRaport)
    elif typeOfRaport == 2:
        raport = HelpRaport.objects.get(id=idOfRaport)
    elif typeOfRaport == 3:
        raport = SpecialResourceRaport.objects.get(id=idOfRaport)
    elif typeOfRaport == 4:
        raport = TradeRaport.objects.get(id=idOfRaport)



    return render(request, 'raportDetail.html', {'raport': raport, 'typeOfRaport': typeOfRaport})
