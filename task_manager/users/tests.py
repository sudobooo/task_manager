from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import ApplicationUsers


class TestApplicationUsers(TestCase):

    fixtures = ['application_users.yaml']

    def setUp(self):
        self.first_user = ApplicationUsers.objects.get(pk=1)
        self.second_user = ApplicationUsers.objects.get(pk=2)
        self.client: Client = Client()

    def test_sign_up(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        username = 'test'
        first_name = 'test'
        last_name = 'test'
        set_password = 'Test123!#'
        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password1': set_password,
            'password2': set_password,
        }

        response = self.client.post(url, new_user, follow=True)
        self.assertRedirects(response, '/login/')

    def test_update(self):
        user = self.first_user
        self.client.force_login(user)
        url = reverse('update_user', args=(user.id, ))

        new_first_name = "Vladimir"
        new_password = 'Test321!#'

        change_user = {
            'first_name': new_first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password1': new_password,
            'password2': new_password,
        }

        response = self.client.post(url, change_user, follow=True)

        self.assertRedirects(response, '/users/')
        changed_user = ApplicationUsers.objects.get(username=user.username)
        self.assertTrue(changed_user.check_password(new_password))

    def test_delete_user(self):
        user = self.second_user
        self.client.force_login(user)
        url = reverse('delete_user', args=(user.id,))

        response = self.client.post(url, follow=True)

        with self.assertRaises(ApplicationUsers.DoesNotExist):
            ApplicationUsers.objects.get(pk=user.id)

        self.assertRedirects(response, '/users/')

    def test_sign_in(self):
        url = reverse('sign_in')

        correct_data = {
            'username': 'yeltsin',
            'password1': 'FakePass654!#'
        }

        response = self.client.post(url, correct_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_sign_out(self):
        url = reverse('sign_out')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
