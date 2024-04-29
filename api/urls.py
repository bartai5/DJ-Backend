from django.urls import path
from .views import *


urlpatterns = [
    path('users/' , getUsers, name='get_users'),
    path('users/<str:pk>/', getUser, name="get_user"),
    path('users/<str:pk>/update/', updateUser, name="update_user"),
    path('users/<str:pk>/delete/', deleteUser, name='delete_user'),
    path('users/create', createUser, name="create_user")
]
