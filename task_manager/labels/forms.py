from django.forms import ModelForm
from task_manager.labels.models import Labels
from django.utils.translation import gettext_lazy


class LabelForm(ModelForm):

    class Meta:
        model = Labels
        fields = ('name', )
        labels = {'name': gettext_lazy('Имя')}
