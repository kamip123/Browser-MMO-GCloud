from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .models import Server
from .models import CityPositions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ExtendedUserCreationForm
from django.http import HttpResponse
from cityMap.models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
from cityMap.models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes


def generate_basic_tables(request):
    building = Barracks()
    building.save()
    building = TownHall()
    building.save()
    building = Roads()
    building.save()
    building = Mines()
    building.save()
    building = PowerPlant()
    building.save()
    building = Farms()
    building.save()
    building = Housing()
    building.save()
    building = Infantry()
    building.save()
    building = HInfantry()
    building.save()
    building = LTanks()
    building.save()
    building = HTanks()
    building.save()
    building = Motorized()
    building.save()
    building = Planes()
    building.save()
    return HttpResponse('Generated tables without problems.')


def fill_village_pos_table(request):
    posx = 1
    posy = 1
    position = CityPositions(villageX=posx, villageY=posy)
    position.save()
    for i in range(1, 1000):
        if posx + 100 > 1000:
            posx = 1
            if posy + 100 > 1000:
                break
            else:
                posy += 100
        else:
            posx += 100

        position = CityPositions(villageX=posx, villageY=posy)
        position.save()

        if posy == 901 and posx == 901:
            break

    return HttpResponse('Generated city positions without problems.')


def main_page(request):
    if request.method == 'POST':
        if 'SignUpForm' in request.POST:
            form = ExtendedUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('miasto/')
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})

        elif 'LogInForm' in request.POST:
            loginForm = AuthenticationForm(data=request.POST)
            form = ExtendedUserCreationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            if loginForm.is_valid():
                user = loginForm.get_user()
                login(request, user)
                servers = Server.objects.all()
                return render(request, 'index.html',
                              {'servers': servers, 'posts': posts, 'form': form, 'loginForm': loginForm})
            else:
                return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})

        elif 'LogOutForm' in request.POST:
            logout(request)
            form = ExtendedUserCreationForm()
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})

    else:
        user = request.user.is_authenticated
        if user:
            loginForm = AuthenticationForm(data=request.POST)
            form = ExtendedUserCreationForm()
            servers = Server.objects.all()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html',
                          {'servers': servers, 'posts': posts, 'form': form, 'loginForm': loginForm})
        else:
            form = ExtendedUserCreationForm()
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})
