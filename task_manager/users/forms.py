
from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import ApplicationUsers


class CreateUserForm(UserCreationForm):

    class Meta:
        model = ApplicationUsers
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
