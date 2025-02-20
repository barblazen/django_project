from categories.models import Category
from books.models import Book
from django.shortcuts import render
from rest_framework.response import Response
new_category = get_object_or_404(Category, id=request.POST.get('category_id'))
Book.objects.filter(id__gt=0).values('id').update(category=new_category)

def making_new_category(request):
    book_ids = request.POST.getlist('book_ids')
    new_category = get_object_or_404(Category, id=request.POST.get('category_id'))
    Book.change_category(book_ids, new_category)
    return Response({"message": "Книги перенесены"})