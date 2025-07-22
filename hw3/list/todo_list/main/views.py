from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def show_list(request: HttpRequest) -> HttpResponse:
    lets_do_it = [
        {'priority': 100, 'task': 'Скласти перелік справ'},
        {'priority': 150, 'task': 'Вивчати Django'},
        {'priority': 1, 'task': 'Подумати про сенс життя'}
    ]

    return render(request, "index.html", {'tasks': lets_do_it})