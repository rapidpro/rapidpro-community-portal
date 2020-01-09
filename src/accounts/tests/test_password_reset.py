from django.test import TestCase
from django.urls import reverse

from . import factories


class PasswordResetTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()
        self.url = reverse('wagtailadmin_password_reset')
        super().setUp()

    def test_get_password_reset_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
