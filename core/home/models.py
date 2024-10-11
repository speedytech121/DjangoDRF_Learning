from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True)
    age = models.IntegerField()
