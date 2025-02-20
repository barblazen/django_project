from django.shortcuts import render

# Create your views here.
from purchases.models import Purchase
from purchases.serializers import PurchaseSerializer
from rest_framework import viewsets

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer