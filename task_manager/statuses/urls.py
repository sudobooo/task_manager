from django.urls import path

from task_manager.statuses.views import (
    ListOfStatuses,
    CreateStatus,
    UpdateStatus,
    DeleteStatus
)

urlpatterns = [
    path('', ListOfStatuses.as_view(), name='list_of_statuses'),
    path('create/', CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete_status'),
]
