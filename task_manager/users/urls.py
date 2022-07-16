from django.urls import path
from task_manager.users.views import ListOfUsers


urlpatterns = [
    path('',  ListOfUsers.as_view(), name='list_of_users'),
]
