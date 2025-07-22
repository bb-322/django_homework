from main.views import *
from django.urls import path

urlpatterns = [
    path('html/', html_response),
    path('text/', text_response),
    path('json/', json_response),
    path('file/', file_response)
]