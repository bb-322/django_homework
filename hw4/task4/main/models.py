from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=64)
    birth_date = models.DateField(blank=True, null=True)


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, default=None)



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    picture = models.FileField(upload_to="product-pictures/", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    customers = models.ManyToManyField(Customer, related_name="products", blank=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
