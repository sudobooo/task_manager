from rest_framework.generics import ListAPIView

from task_manager.api.serializers import ListOfUsersSerializer
from task_manager.users.models import ApplicationUsers


class UsersAPI(ListAPIView):

    serializer_class = ListOfUsersSerializer
    queryset = ApplicationUsers.objects.all()
