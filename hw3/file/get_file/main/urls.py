from main.views import *
from django.urls import path

urlpatterns = [
    path('', send_file),
]