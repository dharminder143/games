from django.urls import path
from api.views import *

urlpatterns = [
    path('product/', ProductList.as_view(), name='Product-ID'),
    

]