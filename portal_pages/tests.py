from django.test import TestCase
from django.utils import timezone

from accounts.models import RapidProUser
from portal_pages.templatetags.portal_extras import make_unique

# Create your tests here.

class TagTests(TestCase):
    # test direct primary key on an object
    # try to use models like django groups

    user1 = RapidProUser.objects.create(
        username="jane@villa.com",
        first_name="Jane",
        last_name="Villanueva",
        is_staff=False,
        is_active=True
        )
    user2 = RapidProUser.objects.create(
        username="xo@villa.com",
        first_name="Xo",
        last_name="Villanueva",
        is_staff=False,
        is_active=True
        )

    print(user1.username)