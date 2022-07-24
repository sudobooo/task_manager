from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import ApplicationUsers

from django.utils.translation import gettext_lazy
from django.db.models import Value
from django.db.models.functions import Concat
from django import forms
import django_filters


class TaskFilter(django_filters.FilterSet):
    statuses = Statuses.objects.values_list('id', 'name', named=True).all()
    status = django_filters.ChoiceFilter(label=gettext_lazy('Статус'),
                                         choices=statuses)

    executors = ApplicationUsers.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True).all()

    executor = django_filters.ChoiceFilter(label=gettext_lazy('Исполнитель'),
                                           choices=executors)

    all_labels = Labels.objects.values_list('id', 'name', named=True).all()

    labels = django_filters.ChoiceFilter(label=gettext_lazy('Метка'),
                                         choices=all_labels)

    my_tasks = django_filters.BooleanFilter(
        label=gettext_lazy('Только свои задачи'),
        widget=forms.CheckboxInput(),
        method='only_my_tasks',
        field_name='my_tasks'
    )

    def only_my_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']
