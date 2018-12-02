from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_map, name='main_page_map'),
    path('city_list/', views.return_citys_list, name='return_citys_list'),
    path('cityListTest/', views.return_citys_list_test, name='return_citys_list_test'),
    path('<int:id_of_city>/', views.city_detail_info, name='city_detail_info'),
    path('<int:id_of_city>/<int:id_of_user>/', views.city_owner_detail_info, name='city_owner_detail_info'),
]
