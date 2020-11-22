from random import randint

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

import tours.data as data


# Create your views here.


def main_view(request):
    random_tours = tuple(randint(1, 6) for _ in range(len(data.tours)))
    tours = {"tours": {}}
    for id in random_tours:
        tours["tours"][id] = data.tours[id]
    return render(request, 'index.html', tours)


def departure_view(request, departure):
    departure_from = data.departures.get(departure, None)
    if not departure_from:
        return HttpResponseServerError("Данной страны отправления не существует")

    tours = {
        "departure": f'{departure_from[0].lower()}{departure_from[1:]}',
        "tours": dict(filter(lambda elem: elem[1]["departure"] == departure, data.tours.items()))
    }
    if not tours["tours"]:
        return render(request, 'departure.html', tours)

    total = len(tours["tours"])
    prices = tuple(map(lambda _tour: _tour["price"], tours["tours"].values()))
    nights = tuple(map(lambda _tour: _tour["nights"], tours["tours"].values()))
    tours["total"] = " ".join((
        f'Найдено {total} тура,',
        f'от {min(prices)} до {max(prices)}₽',
        f'и от {min(nights)} до {max(nights)} ночей',
    ))
    return render(request, 'departure.html', tours)


def tour_view(request, id):
    tour = data.tours.get(id, None)
    if not tour:
        return HttpResponseNotFound(f"Тур с {id} не найден =(")

    departure = data.departures.get(tour["departure"], None)
    if not departure:
        return HttpResponseServerError("Данной страны отправления не существует")

    nights = tour["nights"]

    view_1 = {
        "title": f'{tour["title"]} {int(tour["stars"])*"★"}',
        "price": tour["price"],
        "description": tour["description"],
        "departure": f'{tour["country"]} {departure} {nights} ночей',
        "picture": tour["picture"]
    }
    return render(request, 'tour.html', view_1)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Не верный запрос к серверу =(')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
