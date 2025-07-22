from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def text_response(request: HttpRequest) -> HttpResponse:
    return HttpResponse('text', content_type="text/plain")

def html_response(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>html response</h1>", content_type="text/html")

def file_response(request: HttpRequest):
    content = "file"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    return response

def json_response(request: HttpRequest) -> JsonResponse:
    data = {
        "text": "text"
    }
    return JsonResponse(data)