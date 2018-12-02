from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import BattleRaport, AllianceInvite, HelpRaport, SpecialResourceRaport, TradeRaport

# Create your views here.


@login_required(login_url='../../../../../../../')
def raport_page(request):
    battleraports = BattleRaport.objects.filter(defender=request.user).order_by('created_date')
    alliancereports = AllianceInvite.objects.filter(receiver=request.user).order_by('created_date')
    helpraports = HelpRaport.objects.filter(receiver=request.user).order_by('created_date')
    specialresourceraports = SpecialResourceRaport.objects.filter(receiver=request.user).order_by('created_date')
    tradeeraports = TradeRaport.objects.filter(receiver=request.user).order_by('created_date')
    return render(request, 'indexRaports.html', {'battleraports': battleraports, 'alliancereports': alliancereports, 'helpraports': helpraports, 'specialresourceraports': specialresourceraports, 'tradeeraports': tradeeraports})


@login_required(login_url='../../../../../../../')
def raport_detail_page(request, id_of_raport, type_of_raport):
    if type_of_raport == 0:
        raport = BattleRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 1:
        raport = AllianceInvite.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 2:
        raport = HelpRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 3:
        raport = SpecialResourceRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 4:
        raport = TradeRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()

    return render(request, 'raportDetail.html', {'raport': raport, 'type_of_raport': type_of_raport})
