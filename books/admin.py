from django.contrib import admin

# Register your models here.

from django.contrib import admin
from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("publication_date", "title", "category")
