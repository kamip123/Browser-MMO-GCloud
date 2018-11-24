from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_your_alliance, name='show_your_alliance'),
    path('<int:idOfUser>', views.user_your_alliance_detail_page, name='user_your_alliance_detail_page'),
    path('listOfAlliances/', views.alliance_list_page, name='alliance_list_page'),
    path('listOfAlliances/<int:idOfAlliance>/', views.alliance_detail_page, name='alliance_detail_page'),
    path('listOfAlliances/<int:idOfAlliance>/<int:idOfUser>', views.user_detail_page, name='user_detail_page'),
]
