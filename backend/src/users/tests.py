from rest_framework.test import APITestCase
from users.models import User
from rest_framework import status
from utils.tests import create_user_object, set_super_user
# Create your tests here.


class TestUser(APITestCase):
    def setUp(self):
        self.user = create_user_object('test@gmail.com', 'john', 'doe')

    def test_user_log_in_log_out(self):
        # incorrect credentials
        data = {
            'email': self.user.email,
            'password': 'random_password'
        }

        response = self.client.post(
            '/rest-auth/login/', data, format='json')

        # And that we're returning a 200 created code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(
            'key' in response.data
        )

        response = self.client.post(
            '/rest-auth/logout/', data, format='json')

        # And that we're returning a 200 created code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(
            'Successfully logged out.' in response.data.get('detail'))

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'foobar@example.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        response = self.client.post(
            '/rest-auth/registration/', data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            'Verification e-mail sent.' in response.data.get('detail'))
        self.assertFalse('password' in response.data)
