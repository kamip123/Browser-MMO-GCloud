from django.urls import path
from . import views

urlpatterns = [
    path('', views.raport_page, name='raport_page'),
    path('<int:idOfRaport>/<int:typeOfRaport>', views.raport_detail_page, name='raport_detail_page'),
]
