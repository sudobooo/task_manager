from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import ApplicationUsers


class TestApplicationUsers(TestCase):

    fixtures = ['application_users.yaml', 'tasks.yaml', 'statuses.yaml']

    def setUp(self):
        self.first_user = ApplicationUsers.objects.get(pk=1)
        self.second_user = ApplicationUsers.objects.get(pk=2)
        self.third_user = ApplicationUsers.objects.get(pk=3)
        self.client: Client = Client()

    def test_sign_up(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        new_user = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': 'Test123!#',
            'password2': 'Test123!#',
        }

        response = self.client.post(url, new_user, follow=True)
        self.assertRedirects(response, '/login/')

    def test_update(self):
        user = self.first_user
        self.client.force_login(user)
        url = reverse('update_user', args=(user.id, ))

        change_user = {
            'first_name': "Vladimir",
            'last_name': user.last_name,
            'username': user.username,
            'password1': 'Test321!#',
            'password2': 'Test321!#',
        }

        response = self.client.post(url, change_user, follow=True)
        changed_user = ApplicationUsers.objects.get(username=user.username)

        self.assertRedirects(response, '/users/')
        self.assertTrue(changed_user.check_password('Test321!#'))

    def test_delete_user(self):
        user = self.third_user
        self.client.force_login(user)
        url = reverse('delete_user', args=(user.id,))
        response = self.client.post(url, follow=True)

        with self.assertRaises(ApplicationUsers.DoesNotExist):
            ApplicationUsers.objects.get(pk=user.id)

        self.assertRedirects(response, '/users/')

    def test_sign_in(self):
        url = reverse('sign_in')
        correct_data = {'username': 'yeltsin',
                        'password1': 'FakePass654!#'}
        response = self.client.post(url, correct_data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_sign_out(self):
        url = reverse('sign_out')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_delete_user_with_tasks(self):
        user = self.first_user
        self.client.force_login(user)
        url = reverse('delete_user', args=(user.pk,))
        response = self.client.post(url, follow=True)

        self.assertTrue(
            ApplicationUsers.objects.filter(pk=self.first_user.id).exists()
        )
        self.assertRedirects(response, '/users/')
