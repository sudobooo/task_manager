from task_manager.statuses.forms import StatusesForm
from task_manager.statuses.models import Statuses
from task_manager.mixins import CheckSignInMixin, CheckDeleteMixin

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy
from django.views.generic.edit import DeletionMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    FormView,
    DeleteView
)


class ListOfStatuses(LoginRequiredMixin, CheckSignInMixin, ListView):

    model = Statuses
    template_name = 'statuses/list_of_statuses.html'
    context_object_name = 'statuses'


class CreateStatus(LoginRequiredMixin, CheckSignInMixin,
                   SuccessMessageMixin, CreateView, FormView):

    model = Statuses
    template_name = 'statuses/create_status.html'
    form_class = StatusesForm
    success_message = gettext_lazy('Статус успешно создан')
    success_url = reverse_lazy('list_of_statuses')


class UpdateStatus(LoginRequiredMixin, CheckSignInMixin,
                   SuccessMessageMixin, UpdateView, FormView):

    model = Statuses
    template_name = 'statuses/update_status.html'
    form_class = StatusesForm
    success_url = reverse_lazy('list_of_statuses')
    success_message = gettext_lazy('Статус успешно изменён')


class DeleteStatus(LoginRequiredMixin, CheckSignInMixin, CheckDeleteMixin,
                   SuccessMessageMixin, DeleteView, DeletionMixin):

    model = Statuses
    template_name = 'statuses/delete_status.html'
    error_delete_message = 'Невозможно удалить статус,\
                            потому что он используется'
    success_delete_message = 'Статус успешно удалён'
    redirect_delete_url = 'list_of_statuses'
