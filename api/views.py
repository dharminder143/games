from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from api.serializers import *
from blog.models import *
from rest_framework import filters 
from django_filters import rest_framework 
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth), 
#         }
#         return Response(content)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    permission_classes = [IsAdminUser]
    