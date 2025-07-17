from django.http import HttpRequest, HttpResponse

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse('''
        <p>Hello World!</p>
        <p>Django є одним з найбільших framework на Python</p>
        <hr>'''
    )