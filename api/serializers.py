from rest_framework import serializers
from blog.models import *

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

