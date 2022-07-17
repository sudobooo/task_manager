from task_manager.users.models import ApplicationUsers
from task_manager.users.forms import SignInForm, SignUpForm
from task_manager.mixin import HandleNoPermissionMixin

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.utils.translation import gettext_lazy, gettext
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)


class ListOfUsers(ListView):

    model = ApplicationUsers
    template_name = 'users/list_of_users.html'
    context_object_name = 'application_users'


class SignUp(CreateView, SuccessMessageMixin):

    model = ApplicationUsers
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign_in')
    success_message = gettext_lazy('Пользователь успешно зарегистрирован')


class UpdateUser(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 HandleNoPermissionMixin,
                 UpdateView,
                 FormView, ):

    model = ApplicationUsers
    template_name = 'users/update_user.html'
    form_class = SignUpForm
    success_url = reverse_lazy('list_of_users')
    success_message = gettext_lazy('Пользователь изменён')
    error_message = gettext_lazy('У вас нет прав для изменения другого\
                                  пользователя.')
    no_permission_url = 'list_of_users'

    def test_func(self):
        return self.request.user == self.get_object()


class DeleteUser(LoginRequiredMixin,
                 SuccessMessageMixin,
                 HandleNoPermissionMixin,
                 UserPassesTestMixin,
                 DeleteView,
                 FormView, ):

    model = ApplicationUsers
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('list_of_users')
    success_message = gettext_lazy('Пользователь успешно удалён')
    error_message = gettext_lazy('У вас нет прав для изменения другого\
                                  пользователя.')
    no_permission_url = 'list_of_users'

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, gettext_lazy(self.error_message))
        else:
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)

    def test_func(self):
        return self.request.user == self.get_object()


class SignIn(SuccessMessageMixin, LoginView):

    model = ApplicationUsers
    template_name = 'users/sign_in.html'
    form_class = SignInForm
    next_page = reverse_lazy('main')
    success_message = gettext_lazy('Вы залогинены')


class SignOut(LogoutView, SuccessMessageMixin):

    next_page = reverse_lazy('main')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS,
                             gettext('Вы разлогинены'))
        return super().dispatch(request, *args, **kwargs)
