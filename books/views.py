from pickle import FALSE

from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GetBookAPIView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="author",
                type=str,
                description="Имя автора (фильтрация без учета регистра)",
                required=False
            )
        ],

    )
    def get(self, request):
        author_request = request.query_params.get("author")
        print(author_request)
        if not author_request:
            return Response({"error": "Author is not found"}, status = status.HTTP_400_BAD_REQUEST)

        books = Book.objects.filter(author__icontains=author_request)
        print(books)
        if not books.exists():
            return Response({"error": "Author dont have books"}, status=status.HTTP_400_BAD_REQUEST)
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
@extend_schema(request=BookSerializer)
class PostBookAPIView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PutBookAPIView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeleteBookAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response({"message": "Book deleted"}, status=status.HTTP_204_NO_CONTENT)



class Publish_Book(APIView):
    def publish_books(request):
        book_ids = request.POST.getlist('book_ids')
        Book.objects.filter(id__in=book_ids).update(is_published=True)
        return Response({"message": "Книги опубликованы"})