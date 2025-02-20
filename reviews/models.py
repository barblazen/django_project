
from django.db import models

class Review(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"



