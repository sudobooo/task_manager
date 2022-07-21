from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import ApplicationUsers


class TestTask(TestCase):

    fixtures = ['application_users.yaml', 'statuses.yaml', 'tasks.yaml']

    def setUp(self) -> None:
        self.first_user = ApplicationUsers.objects.get(pk=1)
        self.second_user = ApplicationUsers.objects.get(pk=2)
        self.first_status = Statuses.objects.get(pk=1)
        self.second_status = Statuses.objects.get(pk=2)
        self.first_task = Tasks.objects.get(pk=1)
        self.second_task = Tasks.objects.get(pk=2)

    def test_list_of_tasks(self):
        self.client.force_login(self.first_user)
        response = self.client.get(reverse('list_of_tasks'))
        tasks_list = list(response.context['list_Of_tasks'])

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(tasks_list, [self.first_task,
                                              self.second_task])

    def test_create_tasks(self):
        self.client.force_login(self.first_user)
        task = {
                    'name': 'Написать тесты',
                    'description': 'Тесты к tasks',
                    'author': 1,
                    'executor': 2,
                    'status': 1
                    }

        response = self.client.post(reverse('create_task'), task, follow=True)
        created_task = Tasks.objects.get(name=task['name'])

        self.assertRedirects(response, '/tasks/')
        self.assertEqual(created_task.name, 'Написать тесты')

    def test_update_task(self):
        self.client.force_login(self.first_user)
        url = reverse('update_task', args=(self.first_task.pk,))
        task = {
            'name': 'Обновлённая задача',
            'description': 'Обновлённое описание',
            'author': 2,
            'executor': 1,
            'status': 2
        }

        response = self.client.post(url, task, follow=True)
        created_task = Tasks.objects.get(name=task['name'])

        self.assertRedirects(response, '/tasks/')
        self.assertEqual(created_task.name, 'Обновлённая задача')

    def test_delete_task(self):
        self.client.force_login(self.first_user)
        url = reverse('delete_task', args=(self.first_task.id,))
        response = self.client.post(url, follow=True)

        self.assertRedirects(response, '/tasks/')
