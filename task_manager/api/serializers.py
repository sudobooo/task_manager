from rest_framework.serializers import ModelSerializer

from task_manager.users.models import ApplicationUsers


class ListOfUsersSerializer(ModelSerializer):
    class Meta:
        model = ApplicationUsers
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'date_joined',
                  )
