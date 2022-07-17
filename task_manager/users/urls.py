from django.urls import path
from task_manager.users.views import (
    ListOfUsers,
    SignUp,
    UpdateUser,
    DeleteUser
)


urlpatterns = [
    path('',  ListOfUsers.as_view(), name='list_of_users'),
    path('create/',  SignUp.as_view(), name='sign_up'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete_user'),
]
