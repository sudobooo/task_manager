from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Labels
from task_manager.mixins import CheckSignInMixin, CheckDeleteMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  FormView)


class ListOfLabels(LoginRequiredMixin, CheckSignInMixin, ListView):
    model = Labels
    template_name = 'labels/list_of_labels.html'
    context_object_name = 'labels'


class CreateLabel(SuccessMessageMixin, CheckSignInMixin, CreateView):
    model = Labels
    template_name = 'labels/create_label.html'
    form_class = LabelForm
    success_message = gettext_lazy('Метка успешно создана')
    success_url = reverse_lazy('list_of_labels')


class UpdateLabel(LoginRequiredMixin, CheckSignInMixin,
                  SuccessMessageMixin, UpdateView, FormView):
    model = Labels
    template_name = 'labels/update_label.html'
    form_class = LabelForm
    success_message = gettext_lazy('Метка успешно изменена')
    success_url = reverse_lazy('list_of_labels')


class DeleteLabel(LoginRequiredMixin, CheckSignInMixin, CheckDeleteMixin,
                  SuccessMessageMixin, DeleteView, FormView):
    model = Labels
    template_name = 'labels/delete_label.html'
    error_delete_message = 'Невозможно удалить метку,\
                            потому что она используется'
    success_delete_message = 'Метка успешно удалена'
    redirect_delete_url = 'list_of_labels'
