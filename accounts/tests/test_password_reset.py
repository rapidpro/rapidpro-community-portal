from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from . import factories


class PasswordResetTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()
        self.url = reverse('wagtailadmin_password_reset')
        super().setUp()

    def test_get_password_reset_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_password_reset_page(self):
        response = self.client.post(self.url, {
            'email': self.user.username,
        })
        expected_redirect_url = reverse('wagtailadmin_password_reset_done')
        self.assertRedirects(response, expected_redirect_url)
