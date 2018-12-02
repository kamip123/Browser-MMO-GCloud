from django.urls import path
from . import views

urlpatterns = [
    path('', views.raport_page, name='raport_page'),
    path('<int:id_of_raport>/<int:type_of_raport>', views.raport_detail_page, name='raport_detail_page'),
]
