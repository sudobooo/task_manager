from django.urls import path

from task_manager.labels.views import (ListOfLabels,
                                       CreateLabel,
                                       UpdateLabel,
                                       DeleteLabel)


urlpatterns = [
    path('', ListOfLabels.as_view(), name='list_of_labels'),
    path('create/', CreateLabel.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete_label'),
]
