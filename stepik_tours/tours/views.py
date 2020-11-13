from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Не верный запрос к серверу =(')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
