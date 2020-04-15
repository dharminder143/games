from .models import *

def all_cat(request):
    cat_all=Product.objects.all()[:5]
    # cat_all=list(set(cat_all))
    return {'cat_all':cat_all }