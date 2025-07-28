from django.db import models
from main.fields import AnyCharField

# Create your models here.
class SignUpModel(models.Model):
    username = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    

class LogInModel(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)