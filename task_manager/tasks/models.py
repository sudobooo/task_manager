from django.db import models

from task_manager.statuses.models import Statuses
from task_manager.users.models import ApplicationUsers


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
