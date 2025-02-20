
from django.db import models
from django.db.models import BooleanField


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=35)
    registration_date = models.DateField()
    ROLE_CHOICES = [
        ('author', 'author of the book'),
        ('buyer', 'buyer of the book'),
        ('reader', 'reader of the book'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='reader',
    )
    is_active = BooleanField(default= False)
