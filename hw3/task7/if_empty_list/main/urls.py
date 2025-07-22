from django.urls import path
from main.views import *

urlpatterns = [
    path('', get_list),
]