from .models import *

def all_cat(request):
    cat_all=Product.objects.values('category').distinct()
    return {'cat':cat_all }