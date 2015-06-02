from django.test import TestCase

from wagtail.wagtailcore.models import Page, Site

from portal_pages.models import MarketplaceIndexPage, MarketplaceEntryPage
from portal_pages.views import create_marketplace

# Create your tests here.
# Basing off of tests found here
# https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/tests/test_page_model.py

class MarketplaceEntryPageAddTests(TestCase):

    def setUp(self):
        self.default_site = Site.objects.get(is_default_site=True)
        print(self.default_site)
        
