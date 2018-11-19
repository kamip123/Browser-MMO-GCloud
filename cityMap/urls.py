from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_city, name='main_page_city'),
    path('cityList/', views.main_page_city_list, name='main_page_city_list'),
    path('<int:idOfCity>/', views.main_page_city_id, name='main_page_city_id'),
]
