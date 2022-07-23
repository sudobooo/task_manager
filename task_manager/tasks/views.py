from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Tasks
from task_manager.users.models import ApplicationUsers
from task_manager.mixins import CheckSignInMixin

from django_filters.views import FilterView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)


class ListOfTasks(LoginRequiredMixin, CheckSignInMixin,
                  SuccessMessageMixin, FilterView):
    model = Tasks
    template_name = 'tasks/list_of_tasks.html'
    context_object_name = 'list_Of_tasks'


class CreateTask(LoginRequiredMixin, CheckSignInMixin,
                 SuccessMessageMixin, CreateView):
    model = Tasks
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    success_message = gettext_lazy('Задача успешно создана')
    success_url = reverse_lazy('list_of_tasks')

    def form_valid(self, form):
        author = ApplicationUsers.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, CheckSignInMixin,
                 SuccessMessageMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    success_message = gettext_lazy('Задача успешно изменена')
    success_url = reverse_lazy('list_of_tasks')


class DeleteTask(LoginRequiredMixin, CheckSignInMixin,
                 SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('list_of_tasks')
    success_message = gettext_lazy('Задача успешно удалена')

    def form_valid(self, form):
        if self.request.user != self.get_object().author:
            messages.error(self.request, gettext_lazy('Задачу может удалить\
                                                       только её автор'))
        else:
            super().form_valid(form)
        return redirect(self.success_url)


class ViewTask(LoginRequiredMixin, CheckSignInMixin,
               SuccessMessageMixin, DetailView):
    model = Tasks
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'
