from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_city, name='main_page_city'),
    path('city_list/', views.main_page_city_list, name='main_page_city_list'),
    path('<int:id_of_city>/', views.main_page_city_id, name='main_page_city_id'),
    path('<int:id_of_city>/rozbudowa', views.town_hall_city_id, name='town_hall_city_id'),
    path('<int:id_of_city>/rekrutacja', views.barracks_city_id, name='barracks_city_id'),
    path('<int:id_of_city>/mieszkania', views.housing_city_id, name='housing_city_id'),
    path('colonize/', views.colonize_new_city, name='colonize_new_city'),
]
