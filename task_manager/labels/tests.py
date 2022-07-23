from django.test import TestCase
from django.urls import reverse_lazy, reverse

from task_manager.labels.models import Labels
from task_manager.tasks.models import Tasks
from task_manager.users.models import ApplicationUsers


class TestStatus(TestCase):

    fixtures = ['application_users.yaml',
                'tasks.yaml',
                'labels.yaml',
                'statuses.yaml']

    def setUp(self) -> None:
        self.user = ApplicationUsers.objects.get(pk=1)
        self.first_task = Tasks.objects.get(pk=1)
        self.second_task = Tasks.objects.get(pk=2)
        self.first_label = Labels.objects.get(pk=1)
        self.second_label = Labels.objects.get(pk=2)

    def test_list_of_labels(self):

        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('list_of_labels'))
        labels_list = list(response.context['labels'])

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(labels_list, [self.first_label,
                                               self.second_label])

    def test_create_label(self):

        self.client.force_login(self.user)
        label = {'name': 'Метка'}
        new_data = self.client.post(reverse_lazy('create_label'),
                                    label,
                                    follow=True)
        created_status = Labels.objects.get(name=label['name'])

        self.assertRedirects(new_data, '/labels/')
        self.assertEqual(created_status.name, 'Метка')

    def test_change_label(self):

        self.client.force_login(self.user)
        url = reverse('update_label', args=(self.second_label.pk,))
        label = {'name': 'Другое'}
        response = self.client.post(url, label, follow=True)

        self.assertEqual(Labels.objects.get(pk=self.second_label.id),
                         self.second_label)
        self.assertRedirects(response, '/labels/')

    def test_delete_label(self):

        self.client.force_login(self.user)
        url = reverse_lazy('delete_label', args=(self.second_label.pk,))
        response = self.client.post(url, follow=True)

        with self.assertRaises(Labels.DoesNotExist):
            Labels.objects.get(pk=self.second_label.pk)

        self.assertRedirects(response, '/labels/')

    def test_delete_label_with_task(self):

        self.client.force_login(self.user)
        url = reverse_lazy('delete_label', args=(self.first_label.pk,))
        response = self.client.post(url, follow=True)

        self.assertTrue(Labels.objects.filter(pk=self.first_label.id).exists())
        self.assertRedirects(response, '/labels/')

    def test_status_list_without_authorization(self):

        response = self.client.get(reverse_lazy('list_of_labels'))
        self.assertRedirects(response, '/login/')
