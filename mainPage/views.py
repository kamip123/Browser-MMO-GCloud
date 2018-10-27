from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .models import Server
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def main_page(request):
    if request.method == 'POST':
        if 'SignUpForm' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('miasto/')
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})

        elif 'LogInForm' in request.POST:
            loginForm = AuthenticationForm(data=request.POST)
            form = UserCreationForm()
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
            form = UserCreationForm()
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})

    else:
        user = request.user.is_authenticated
        if user:
            loginForm = AuthenticationForm(data=request.POST)
            form = UserCreationForm()
            servers = Server.objects.all()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html',
                          {'servers': servers, 'posts': posts, 'form': form, 'loginForm': loginForm})
        else:
            form = UserCreationForm()
            loginForm = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'loginForm': loginForm})
