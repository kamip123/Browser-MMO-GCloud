from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_your_alliance, name='show_your_alliance'),
    path('listOfAlliances/', views.alliance_list_page, name='alliance_list_page'),
    path('listOfAlliances/<int:idOfAlliance>/', views.alliance_detail_page, name='alliance_detail_page'),
]
