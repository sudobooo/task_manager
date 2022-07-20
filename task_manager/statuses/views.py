from task_manager.statuses.forms import StatusesForm
from task_manager.statuses.models import Statuses

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy, gettext
from django.views.generic.edit import DeletionMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    FormView,
    DeleteView
)


class ListOfStatuses(LoginRequiredMixin, ListView):

    model = Statuses
    template_name = 'statuses/list_of_statuses.html'
    context_object_name = 'statuses'
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin,
                   CreateView, FormView):

    model = Statuses
    template_name = 'statuses/create_status.html'
    form_class = StatusesForm
    success_message = gettext_lazy('Статус успешно создан')
    success_url = reverse_lazy('list_of_statuses')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin,
                   UpdateView, FormView):

    model = Statuses
    template_name = 'statuses/update_status.html'
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Статус успешно изменён')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin,
                   DeleteView, DeletionMixin):

    model = Statuses
    template_name = 'statuses/delete_status.html'
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Статус успешно удалён')
    redirect_field_name = 'sign_in'

    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста,\
                                              выполните вход.'))
        return redirect(self.redirect_field_name)
