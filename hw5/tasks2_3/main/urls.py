from django.urls import path
from main.views import *

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='login'),
    path('model-login/', LoginWModel.as_view(), name='login'),
]