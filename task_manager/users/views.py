from django.views.generic.list import ListView
from task_manager.users.models import ApplicationUsers
from task_manager.users.forms import CreateUserForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy


class ListOfUsers(ListView):
    model = ApplicationUsers
    template_name = 'users/list_of_users.html'
    context_object_name = 'application_users'


class CreateUser(CreateView, SuccessMessageMixin):
    model = ApplicationUsers
    template_name = 'users/create_user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('list_of_users')
    success_message = gettext_lazy('Пользователь создан')
