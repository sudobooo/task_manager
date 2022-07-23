from django.db import models

from task_manager.statuses.models import Statuses
from task_manager.users.models import ApplicationUsers
from task_manager.labels.models import Labels


class Tasks(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    status = models.ForeignKey(Statuses,
                               on_delete=models.PROTECT,
                               null=True,
                               related_name='task_status')
    author = models.ForeignKey(ApplicationUsers,
                               on_delete=models.PROTECT,
                               null=False,
                               related_name='task_author')
    executor = models.ForeignKey(ApplicationUsers,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT,
                                 related_name='task_executor')
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels,
                                    related_name='task_label',
                                    blank=True,
                                    through='TaskLabels',
                                    through_fields=('task', 'label'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class TaskLabels(models.Model):

    task = models.ForeignKey(Tasks,
                             on_delete=models.CASCADE)
    label = models.ForeignKey(Labels,
                              on_delete=models.PROTECT)
