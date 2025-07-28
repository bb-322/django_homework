from django.db import models

# Create your models here.
class ReviewModel(models.Model):
    email = models.EmailField(max_length=255)
    description = models.CharField(max_length=500)
    rating = models.IntegerField()
    phone_number = models.IntegerField()
    picture = models.FileField()