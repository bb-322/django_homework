from django.urls import path
from chars.views import *

urlpatterns = [
    path('', welcome),
    path('char/luke', luke),
    path('char/leia', leia),
    path('char/han', han)
]