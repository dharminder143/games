from django.urls import path
from . import views

urlpatterns = [
    path('', views.product,name='product'),
    path('post', views.post,name='post'),
    path('simple_upload/', views.simple_upload,name='simple_upload'),
    path('search/', views.search, name='search'),  
    path('signin/',views.signup,name='signup'),

]