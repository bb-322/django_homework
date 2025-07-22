from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def show_per(request:HttpRequest) -> HttpResponse:
    per_list = [
        {'name': 'Шаддам IV', 'surname': 'Корріно'},
        {'name': 'Стать', 'surname': 'Атрейдес'},
        {'name': 'Франклін', 'surname': 'Герберт'}
    ]

    return render(request, "index.html", {'people': per_list})