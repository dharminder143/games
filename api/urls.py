from django.urls import path 
from api.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('product/', ProductList.as_view(), name='Product-ID'),
    path('userlist/', UserList.as_view(), name='UserList'),
    path('auth/<pk>', UserDetail.as_view(), name='UserDetail'),
    # path('auth/', ExampleView.as_view(), name='ExampleView'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    

]
