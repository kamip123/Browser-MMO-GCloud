from django.shortcuts import render

# Create your views here.


def main_page_city(request):
    return render(request, 'indexCityMap.html')
