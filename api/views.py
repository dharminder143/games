
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from api.serializers import ( ItemSerializer )
from blog.models import *
from rest_framework import filters 
from django_filters import rest_framework 

class ProductFilter(rest_framework.FilterSet):
    class Meta:
        model = Product
        fields = ['category']

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['category','gamename','vendor','id']