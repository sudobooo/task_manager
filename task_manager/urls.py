from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from task_manager.users.views import SignIn, SignOut

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('users/', include('task_manager.users.urls'), name='users'),
    path('statuses/', include('task_manager.statuses.urls'), name='statuses'),
    path('labels/', include('task_manager.labels.urls'), name='labels'),
    path('tasks/', include('task_manager.tasks.urls'), name='tasks'),
    path('login/', SignIn.as_view(), name='sign_in'),
    path('logout/', SignOut.as_view(), name='sign_out'),
    path('admin/', admin.site.urls),
]
