from rest_framework import request

from books.models import Book
from rest_framework.response import Response
discount = float(request.POST.get('discount', 0))
Book.objects.filter(id__gt=0).values('id').update(price=F('price') * (1 - discount / 100))

def apply_discount(request):
    book_ids = request.POST.getlist('book_ids')
    Book.apply_discount(book_ids, discount)
    return Response({"message": "Скидка применена"})