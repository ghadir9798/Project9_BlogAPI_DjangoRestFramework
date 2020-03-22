from django.urls import path
from . import views

app_name = 'users-api'
urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(), name='register' ),
    path('login/', views.UserLoginAPIView.as_view(), name='login' ),
]
