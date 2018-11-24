from django.urls import path
from . import views

urlpatterns = [
    path('', views.premium_page, name='premium_page'),
    path('platnosc/', views.premium_platnosc, name='premium_platnosc'),
    path('historia/', views.premium_history, name='premium_history'),
]