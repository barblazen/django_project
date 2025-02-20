from users.models import User
from django.shortcuts import render
from rest_framework.response import Response
User.objects.filter(id__gt=0).values('id').update(is_active=False)
def user_blocking(request):
    user_ids = request.POST.getlist('user_ids')
    User.objects.filter(id__in=user_ids).update(is_active=False)
    return Response({"message": "Пользователи заблокированы"})