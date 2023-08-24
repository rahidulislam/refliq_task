from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegisterView,UserLoginView
app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('token/', UserLoginView.as_view(), name='user_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
