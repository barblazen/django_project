"""
URL configuration for onlinestore_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet, PostBookAPIView, GetBookAPIView, PutBookAPIView, DeleteBookAPIView
from onlinestore_project import settings
from reviews.models import Review
from categories.models import Category
from purchases.models import Purchase
from reviews.views import ReviewViewSet
from categories.views import CategoryViewSet
from purchases.views import PurchaseViewSet
from users.views import UserView, BaseUserView, ExtendedUserView
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'reviews', ReviewViewSet)
#router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'purchases', PurchaseViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_api_view/', GetBookAPIView.as_view()),
    path('post_api_view/', PostBookAPIView.as_view()),
    path("users/", BaseUserView.as_view(), name="user-list"),
    path("users/<int:pk>/", ExtendedUserView.as_view(), name="user-detail"),
    path("books/", GetBookAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/", PutBookAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/", PostBookAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/", DeleteBookAPIView.as_view(), name="book-detail"),
]

if settings.USE_BROWSABLE_API:
    urlpatterns += [
        path("docs/", SpectacularAPIView.as_view(), name="docs"),
        path("", SpectacularSwaggerView.as_view(url_name="docs")),
    ]
urlpatterns += router.urls


