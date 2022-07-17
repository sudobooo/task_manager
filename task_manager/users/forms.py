
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from task_manager.users.models import ApplicationUsers


class SignUpForm(UserCreationForm):

    class Meta:
        model = ApplicationUsers
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class SignInForm(AuthenticationForm):
    username = ApplicationUsers.username
    password = ApplicationUsers.password
    fields = ['username', 'password1']
