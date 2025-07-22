from django.urls import path
from main.views import show_list

urlpatterns = [
    path('', show_list),
]