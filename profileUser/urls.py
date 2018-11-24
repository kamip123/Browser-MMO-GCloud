from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('zmienHaslo/', views.haslo_page, name='haslo_page'),
    path('zmienEmail/', views.email_page, name='email_page'),
    path('zmienProfil/', views.profilowe_page, name='profilowe_page'),
]
