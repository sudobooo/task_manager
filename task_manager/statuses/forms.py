from django.forms import ModelForm
from task_manager.statuses.models import Statuses
from django.utils.translation import gettext_lazy


class StatusesForm(ModelForm):

    class Meta:
        model = Statuses
        fields = ['name']
        labels = {'name': gettext_lazy('Имя')}
