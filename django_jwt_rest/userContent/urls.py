from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,  UserDetail, UpdateProfileView
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('users/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='register'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    path('user/<int:pk>/', UserDetail.as_view()),
    path('users/<int:pk>/', UpdateProfileView.as_view())
]
