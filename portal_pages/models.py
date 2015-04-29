from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.models import Image
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


"""
The following models may be shared across multiple other models
"""


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "countries"


class FocusArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class TechFirm(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


"""
Page models
"""


class HomePage(Page):
    home_content = RichTextField()

HomePage.content_panels = [
    FieldPanel('title'),
    FieldPanel('home_content'),
    InlinePanel('hero_items', label='Hero Images'),
    InlinePanel('highlights', label='Highlights'),
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


class HighlightItem(Orderable, models.Model):
    home_page = ParentalKey(HomePage, related_name='highlights')
    title = models.CharField(max_length=255)
    blurb = RichTextField()
    icon = models.ForeignKey(Image)
    target_page = models.ForeignKey(Page)

HighlightItem.panels = [
    FieldPanel('title'),
    PageChooserPanel('target_page'),
    FieldPanel('blurb'),
    ImageChooserPanel('icon'),
]


class CMSPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

CMSPage.content_panels = [
    FieldPanel('title'),
    StreamFieldPanel('body'),
]

# CaseStudy index page


class CaseStudyIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def casestudies(self):
        # Get list of live casestudy pages that are descendants of this page
        casestudies = CaseStudyPage.objects.live().descendant_of(self)

        # Order by most recent date first
        casestudies = casestudies.order_by('-date')

        # TODO: filter out case studies that have post dates after today's date

        return casestudies

    def get_context(self, request):
        # Get casestudies
        casestudies = self.casestudies

        # Filter by country
        country = request.GET.get('country')
        if country:
            casestudies = casestudies.filter(countries__country__name=country)

        # Filter by focus area
        focus_area = request.GET.get('focus_area')
        if focus_area:
            casestudies = casestudies.filter(focus_areas__focusarea__name=focus_area)

        # Filter by organization
        organization = request.GET.get('organization')
        if organization:
            casestudies = casestudies.filter(organizations__organization__name=organization)

        # Filter by tech firm
        tech_firm = request.GET.get('tech_firm')
        if tech_firm:
            casestudies = casestudies.filter(tech_firms__techfirm__name=tech_firm)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(casestudies, 6)  # Show 6 casestudies per page
        try:
            casestudies = paginator.page(page)
        except PageNotAnInteger:
            casestudies = paginator.page(1)
        except EmptyPage:
            casestudies = paginator.page(paginator.num_pages)

        # Update template context
        context = super(CaseStudyIndexPage, self).get_context(request)
        context['casestudies'] = casestudies
        return context

CaseStudyIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
]

CaseStudyIndexPage.promote_panels = Page.promote_panels


# Case Study Page

class CaseStudyPage(Page):
    summary = RichTextField()
    date = models.DateField("Post date")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    downloadable_package = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('summary'),
    )

    @property
    def casestudy_index(self):
        # Find closest ancestor which is a casestudy index
        return self.get_ancestors().type(CaseStudyIndexPage).last()

CaseStudyPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('summary', classname="full"),
    ImageChooserPanel('hero_image'),
    DocumentChooserPanel('downloadable_package'),
    InlinePanel(CaseStudyPage, 'focus_areas', label="Focus Areas"),
    InlinePanel(CaseStudyPage, 'countries', label="Countries"),
    InlinePanel(CaseStudyPage, 'organizations', label="Organizations"),
    InlinePanel(CaseStudyPage, 'tech_firms', label="Tech Firms"),
]


# The following children of Case Study use through-model
# Desribed in M2M issue work-around
# https://github.com/torchbox/wagtail/issues/231

class CountryCaseStudy(Orderable, models.Model):
    country = models.ForeignKey(Country, related_name="+")
    page = ParentalKey(CaseStudyPage, related_name='countries')
    panels = [
        FieldPanel('country'),
    ]


class FocusAreaCaseStudy(Orderable, models.Model):
    focusarea = models.ForeignKey(FocusArea, related_name="+")
    page = ParentalKey(CaseStudyPage, related_name='focus_areas')
    panels = [
        FieldPanel('focusarea'),
    ]


class OrganizationCaseStudy(Orderable, models.Model):
    organization = models.ForeignKey(Organization, related_name="+")
    page = ParentalKey(CaseStudyPage, related_name='organizations')
    panels = [
        FieldPanel('organization'),
    ]


class TechFirmCaseStudy(Orderable, models.Model):
    techfirm = models.ForeignKey(TechFirm, related_name="+")
    page = ParentalKey(CaseStudyPage, related_name='tech_firms')
    panels = [
        FieldPanel('techfirm'),
    ]
