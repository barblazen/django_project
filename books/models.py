from django.db import models

# Create your models here.
class Book(models.Model):
    price = models.FloatField()
    publication_date = models.DateField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField()