from django.urls import path
from task_manager.users.views import (
    ListOfUsers,
    CreateUser,
    UpdateUser,
    DeleteUser
)


urlpatterns = [
    path('',  ListOfUsers.as_view(), name='list_of_users'),
    path('create/',  CreateUser.as_view(), name='create_user'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete_user'),
]
