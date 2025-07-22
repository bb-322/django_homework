from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def get_list(request:HttpRequest) -> HttpResponse:
    latest_question_list = [
        {'id': 1, 'question_text': "У чому сенс життя?"},
        {'id': 2, 'question_text': "Що первинне: дух чи матерія?"},
        {'id': 3, 'question_text': "Чи існує свобода волі?"}
    ]
    return render(request, 'index.html', {'questions': latest_question_list})