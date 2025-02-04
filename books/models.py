from django.db import models

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from reviews.models import Category, Review



# Create your models here.
class Book(models.Model):
    price = models.FloatField()
    publication_date = models.DateField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True),
    review = models.CharField(max_length=250)
    is_available = models.BooleanField()