from import_export import resources
from .models import Product

class PersonResource(resources.ModelResource):
    class Meta:
        model = Product