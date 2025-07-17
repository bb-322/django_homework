from django.http import HttpRequest, HttpResponse

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>main page</h1>')