from books.models import Book
from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
Book.objects.filter(id__gt=0).values('id').update(is_published=True)

class Publish_Book(APIView):
    def publish_books(request):
        book_ids = request.POST.getlist('book_ids')
        Book.objects.filter(id__in=book_ids).update(is_published=True)
        return Response({"message": "Книги опубликованы"})