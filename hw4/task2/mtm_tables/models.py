from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=100)
    workers = models.ManyToManyField(Worker, related_name="projects")