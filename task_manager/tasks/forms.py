from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from task_manager.tasks.models import Tasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'status', 'executor', 'labels')
        labels = {'name': gettext_lazy('Имя'),
                  'description': gettext_lazy('Описание'),
                  'status': gettext_lazy('Статус'),
                  'executor': gettext_lazy('Исполнитель'),
                  'labels': gettext_lazy('Метки')
                  }
