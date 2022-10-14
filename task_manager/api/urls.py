from django.urls import path

from task_manager.api.views import UsersAPI

urlpatterns = [
    path('users', UsersAPI.as_view()),
]