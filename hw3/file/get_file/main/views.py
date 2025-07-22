from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def send_file(request: HttpRequest):
    content = "Ось ваш файл"
    response = HttpResponse(content, content_type='text/plain', status=227)
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    return response