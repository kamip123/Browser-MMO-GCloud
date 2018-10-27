from django.shortcuts import render

# Create your views here.


def main_page_map(request):
    return render(request, 'indexWorldMap.html')
