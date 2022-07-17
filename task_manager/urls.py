from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from task_manager.users.views import SignIn, SignOut

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('users/', include('task_manager.users.urls'), name='list_of_users'),
    path('login/', SignIn.as_view(), name='sign_in'),
    path('logout/', SignOut.as_view(), name='sign_out'),
    path('admin/', admin.site.urls),
]
