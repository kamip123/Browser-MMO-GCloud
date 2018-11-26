from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.main_page_city, name='main_page_city'),
    path('cityList/', views.main_page_city_list, name='main_page_city_list'),
    path('<int:idOfCity>/', views.main_page_city_id, name='main_page_city_id'),
    path('<int:idOfCity>/rozbudowa', views.town_hall_city_id, name='town_hall_city_id'),
    path('<int:idOfCity>/rekrutacja', views.barracks_city_id, name='barracks_city_id'),
    #path('<int:idOfCity>/rekrutacja', TemplateView.as_view(template_name='barracks.html')),
    path('colonize/', views.colonize_new_city, name='colonize_new_city'),
]
