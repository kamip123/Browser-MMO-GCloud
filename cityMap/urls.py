from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_city, name='main_page_city'),
]