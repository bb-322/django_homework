from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def welcome(request: HttpRequest):
    return render(request, "index.html")

def luke(request: HttpRequest):
    context = {
        'name': 'Люк Скайуокер',
        'text': 'один із головних персонажів всесвіту «Зоряних війн», джедай, син сенатора з Набу Падме Амідали Наберрі та лицаря-джеда Енакіна Скайуокера.'
    }

    return render(request, "char.html", context)

def leia(request: HttpRequest):
    context = {
        'name': 'Лея Органа',
        'text': 'дочка лицаря-джеда Енакіна Скайуокера та сенатора Падме Амідали Наберрі.'
    }

    return render(request, "char.html", context)

def han(request: HttpRequest):
    context = {
        'name': 'Хан Соло',
        'text': "пілот космічного корабля «Тисячолітній сокіл», його бортмеханіком та другим пілотом є вуки на ім'я Чубакка."
    }

    return render(request, "char.html", context)