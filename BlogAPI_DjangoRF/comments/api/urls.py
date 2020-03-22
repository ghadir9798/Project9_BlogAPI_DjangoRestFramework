from django.urls import path
from . import views

app_name = 'comments-api'
urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name='list' ),
    path('create/', views.CommentCreateAPIView.as_view(), name='create' ),
    path('<int:pk>/', views.CommentDetailAPIView.as_view(), name='detail' ),
    # path('create/', views.PostCreateAPIView.as_view(), name='create' ),
]
