
from django.db import models
from books.models import Book
from users.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="purchases")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


    def save(self, *args, **kwargs):
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase by {self.user.username} - {self.book.title} ({self.quantity})"
