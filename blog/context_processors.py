from .models import *
from django.db.models import Q 


def all_cat(request):
    cat_all=Product.objects.values('category').distinct()
    pro=Product.objects.filter()
    return {'cat':cat_all,'pro':pro }