from django.urls import path
from app.views import Page

urlpatterns = [
    path('weather/', Page.as_view(), name='page')
]