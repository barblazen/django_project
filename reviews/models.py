
from django.db import models

class Review(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name