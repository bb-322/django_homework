from django.urls import path
from main.views import ReviewPage

urlpatterns = [
    path('', ReviewPage.as_view()),
]