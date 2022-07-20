from django.contrib import admin

from task_manager.tasks.models import Tasks

admin.site.register(Tasks)
