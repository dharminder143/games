from rest_framework import serializers
from blog.models import *
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'gamename',
            'vendor',
            'GameURL',
            'IMGURL',
            'created_at',
        )

class UserSerializer(serializers.ModelSerializer):
    # Product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
