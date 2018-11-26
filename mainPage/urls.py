from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('fillTablePos/', views.fill_village_pos_table, name='fill_village_pos_table'),
    path('thingsStats/', views.generate_basic_tables, name='generate_basic_tables'),
]
