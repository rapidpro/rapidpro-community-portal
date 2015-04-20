from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.models import Image
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


class HomePage(Page):
    home_content = RichTextField()

HomePage.content_panels = [
    FieldPanel('title'),
    FieldPanel('home_content'),
    InlinePanel('hero_items', label='Hero Images'),
]


class HomePageHeroImageItem(Orderable, models.Model):
    home_page = ParentalKey(HomePage, related_name='hero_items')
    blurb = RichTextField()
    target_page = models.ForeignKey(Page)
    hero_image = models.ForeignKey(Image)

HomePageHeroImageItem.panels = [
    FieldPanel('blurb'),
    PageChooserPanel('target_page'),
    ImageChooserPanel('hero_image'),
]
