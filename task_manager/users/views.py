from django.views.generic.list import ListView
from task_manager.users.models import ApplicationUsers


class ListOfUsers(ListView):
    model = ApplicationUsers
    template_name = 'users/list_of_users.html'
    context_object_name = 'application_users'
