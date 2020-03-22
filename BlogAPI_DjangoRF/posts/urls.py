from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='list' ),
    path('create/', views.post_create, name='create' ),
    path('<int:id>/', views.post_detail, name='detail' ),
    path('<int:id>/edit/', views.post_update, name='update' ),
    path('<int:id>/delete/', views.post_delete, name='delete' ),
]
