from django.contrib.auth import get_user_model
from django.test import TestCase

from . import factories

USER_MODEL = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()
        super().setUp()

    def test_get_full_name(self):
        self.assertEqual(
            '{0} {1}'.format(self.user.first_name, self.user.last_name),
            self.user.get_full_name()
        )

    def test_no_username(self):
        with self.assertRaises(ValueError):
            factories.UserFactory(username='')

    def test_access_email(self):
        self.assertEqual(self.user.username, self.user.email)
