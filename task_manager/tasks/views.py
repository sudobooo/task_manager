from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Tasks
from task_manager.users.models import ApplicationUsers

from django.contrib import messages
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class ListOfTasks(LoginRequiredMixin,
                  SuccessMessageMixin,
                  FilterView):
    model = Tasks
    template_name = 'tasks/list_of_tasks.html'
    context_object_name = 'list_Of_tasks'
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class CreateTask(SuccessMessageMixin, CreateView):
    model = Tasks
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    success_message = gettext_lazy('Задача успешно создана')
    success_url = reverse_lazy('list_of_tasks')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)

    def form_valid(self, form):
        author = ApplicationUsers.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTask(SuccessMessageMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    success_message = gettext_lazy('Задача успешно изменена')
    success_url = reverse_lazy('list_of_tasks')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class DeleteTask(LoginRequiredMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = Tasks
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('list_of_tasks')
    success_message = gettext_lazy('Задача успешно удалена')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class ViewTask(LoginRequiredMixin,
               SuccessMessageMixin,
               DetailView):
    model = Tasks
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)
