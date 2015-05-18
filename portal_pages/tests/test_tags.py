from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from . import factories

USER_MODEL = get_user_model()

from accounts.models import RapidProUser
from portal_pages.templatetags.portal_extras import make_unique

# Create your tests here.

class TagTests(TestCase):

    def setUp(self):
        self.user1 = factories.UserFactory()
        self.user2 = factories.UserFactory()
        super().setUp()

    def test_make_unique_filter(self):
        RapidProUser.objects.all().update(last_name="Villanueva")

        users_distinct_last = make_unique(RapidProUser.objects.all(), "last_name")

        self.assertEqual(users_distinct_last.count(), 1)