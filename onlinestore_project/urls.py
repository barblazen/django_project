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
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter


from onlinestore_project import settings
from users.views import UserView

router = DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
]
if settings.USE_BROWSABLE_API:
    urlpatterns += [
        path("__docs__/", SpectacularAPIView.as_view(), name="__docs__"),
        path("", SpectacularSwaggerView.as_view(url_name="__docs__")),
    ]

urlpatterns += router.urls