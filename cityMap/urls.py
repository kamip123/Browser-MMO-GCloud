from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_city, name='main_page_city'),
    path('cityList/', views.main_page_city_list, name='main_page_city_list'),
    path('<int:idOfCity>/', views.main_page_city_id, name='main_page_city_id'),
    path('<int:idOfCity>/rozbudowa', views.town_hall_city_id, name='town_hall_city_id'),
    path('<int:idOfCity>/rekrutacja', views.barracks_city_id, name='barracks_city_id'),
]
