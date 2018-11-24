from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_map, name='main_page_map'),
    path('cityList/', views.return_citys_list, name='return_citys_list'),
    path('cityListTest/', views.return_citys_list_test, name='return_citys_list_test'),
    path('<int:idOfCity>/', views.city_detail_info, name='city_detail_info'),
    path('<int:idOfCity>/<int:idOfUser>/', views.city_owner_detail_info, name='city_owner_detail_info'),
]
