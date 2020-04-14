from django.urls import path
from . import views

urlpatterns = [
    path('', views.product,name='product'),
    path('post', views.post,name='post'),
    path('simple_upload/', views.simple_upload,name='simple_upload'),
    path('search/', views.search, name='search'),  
    path('action-games/',views.post_action,name='post_action')

]