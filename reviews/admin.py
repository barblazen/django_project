from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "comment")
