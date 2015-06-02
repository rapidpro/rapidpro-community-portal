from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.models import Image
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, PageChooserPanel, InlinePanel,
    StreamFieldPanel, MultiFieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

from accounts.models import RapidProUser


"""
The following models may be shared across multiple other models
"""


@register_snippet
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    longitude = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "countries"


@register_snippet
class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


@register_snippet
class FocusArea(models.Model):
    name = models.CharField(max_length=255, unique=True)

    panels = [FieldPanel('name')]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


@register_snippet
class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


@register_snippet
class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


@register_snippet
class Expertise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'expertise'


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True


class TopImage(models.Model):
    top_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('top_image'),
    ]

    class Meta:
        abstract = True


@register_snippet
class DefaultTopImage(models.Model):
    default_top_image = models.ForeignKey(
        'wagtailimages.Image'
    )

    panels = [
        ImageChooserPanel('default_top_image'),
    ]

    def __str__(self):
        return self.default_top_image.title


"""
Page models
"""


class HomePage(Page):
    featured_case_study = models.ForeignKey(
        'portal_pages.CaseStudyPage', blank=True, null=True, on_delete=models.SET_NULL)
    featured_case_study_blurb = RichTextField(blank=True, default='')
    youtube_video_id = models.CharField(max_length=512, blank=True, default='')
    youtube_video_title = models.CharField(max_length=512, blank=True, default='')
    youtube_blurb = RichTextField(blank=True, default='')

HomePage.content_panels = [
    MultiFieldPanel(
        [FieldPanel('title')],
        heading='Title',
        classname='collapsible collapsed',
    ),
    MultiFieldPanel(
        [InlinePanel('hero_items')],
        heading='Hero images',
        classname='collapsible collapsed',
    ),
    MultiFieldPanel(
        [InlinePanel('highlights')],
        heading='Highlights',
        classname='collapsible collapsed',
    ),
    MultiFieldPanel(
        [
            FieldPanel('youtube_video_id'),
            FieldPanel('youtube_video_title'),
            FieldPanel('youtube_blurb'),
        ],
        heading='Youtube video information',
        classname='collapsible collapsed',
    ),
    MultiFieldPanel(
        [
            PageChooserPanel('featured_case_study', 'portal_pages.CaseStudyPage'),
            FieldPanel('featured_case_study_blurb'),
        ],
        heading='Featured case study',
        classname='collapsible collapsed',
    ),
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


class CMSPage(Page, TopImage):
    body = RichTextField(blank=True, default='')

CMSPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('body'),
]


# Marketplace index page


class MarketplaceIndexPage(Page, TopImage):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    subpage_types = ['portal_pages.MarketplaceEntryPage']

    @property
    def marketplace_entries(self):
        # Get list of live marketplace entry pages that are descendants of this page
        marketplace_entries = MarketplaceEntryPage.objects.live().descendant_of(self)

        # Order by most recent date first
        marketplace_entries = marketplace_entries.order_by('-date_start')

        # TODO: filter out marketplace entries that have post dates after today's date
        return marketplace_entries

    def get_context(self, request):
        # Get marketplace_entries
        marketplace_entries = self.marketplace_entries

        # Filter by region
        region = request.GET.get('region')
        if region:
            marketplace_entries = marketplace_entries.filter(regions__region__name=region)

        # Filter by country
        country = request.GET.get('country')
        if country:
            marketplace_entries = marketplace_entries.filter(countries__country__name=country)

        # Filter by service
        service = request.GET.get('service')
        if service:
            marketplace_entries = marketplace_entries.filter(services__service__name=service)

        # Filter by expertise
        expertise = request.GET.get('expertise')
        if expertise:
            marketplace_entries = marketplace_entries.filter(expertise_tags__expertise__name=expertise)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(marketplace_entries, 6)  # Show 6 marketplace_entries per page
        try:
            marketplace_entries = paginator.page(page)
        except PageNotAnInteger:
            marketplace_entries = paginator.page(1)
        except EmptyPage:
            marketplace_entries = paginator.page(paginator.num_pages)

        # Update template context
        context = super(MarketplaceIndexPage, self).get_context(request)
        context['marketplace_entries'] = marketplace_entries
        return context

MarketplaceIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    MultiFieldPanel(TopImage.panels, "hero image"),
]

MarketplaceIndexPage.promote_panels = Page.promote_panels


# Marketplace Entry Page


class MarketplaceEntryPage(Page, ContactFields, TopImage):
    biography = RichTextField(blank=True)
    date_start = models.DateField("Company Start Date")

    @property
    def marketplace_index(self):
        # Find closest ancestor which is a casestudy index
        return self.get_ancestors().type(MarketplaceIndexPage).last()

MarketplaceEntryPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date_start'),
    FieldPanel('biography', classname="full"),
    MultiFieldPanel(TopImage.panels, "branding banner"),
    MultiFieldPanel(ContactFields.panels, "Contact"),
    InlinePanel(MarketplaceEntryPage, 'services', label="Services"),
    InlinePanel(MarketplaceEntryPage, 'expertise_tags', label="Expertise"),
    InlinePanel(MarketplaceEntryPage, 'regions', label="Regions of Experience"),
    InlinePanel(MarketplaceEntryPage, 'countries', label="Countries of Experience"),
]


class CountryMarketplaceEntry(Orderable, models.Model):
    country = models.ForeignKey(Country, related_name="+")
    page = ParentalKey(MarketplaceEntryPage, related_name='countries')
    panels = [
        FieldPanel('country'),
    ]


class RegionMarketplaceEntry(Orderable, models.Model):
    region = models.ForeignKey(Region, related_name="+")
    page = ParentalKey(MarketplaceEntryPage, related_name='regions')
    panels = [
        FieldPanel('region'),
    ]


class ServiceMarketplaceEntry(Orderable, models.Model):
    service = models.ForeignKey(Service, related_name="+")
    page = ParentalKey(MarketplaceEntryPage, related_name='services')
    panels = [
        FieldPanel('service'),
    ]


class ExpertiseMarketplaceEntry(Orderable, models.Model):
    expertise = models.ForeignKey(Expertise, related_name="+")
    page = ParentalKey(MarketplaceEntryPage, related_name='expertise_tags')
    panels = [
        FieldPanel('expertise'),
    ]


# CaseStudy index page


class CaseStudyIndexPage(Page, TopImage):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    subpage_types = ['portal_pages.CaseStudyPage']

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

        # Filter by region
        region = request.GET.get('region')
        if region:
            casestudies = casestudies.filter(regions__region__name=region)

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

        # Filter by marketplace entry
        marketplace = request.GET.get('marketplace')
        if marketplace:
            casestudies = casestudies.filter(marketplace_entry__title=marketplace)

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
    MultiFieldPanel(TopImage.panels, "hero image"),
]

CaseStudyIndexPage.promote_panels = Page.promote_panels


# Case Study Page


class CaseStudyPage(Page, TopImage):
    summary = RichTextField()
    date = models.DateField("Create date")
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

    marketplace_entry = models.ForeignKey(
        'portal_pages.MarketplaceEntryPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    @property
    def casestudy_index(self):
        # Find closest ancestor which is a casestudy index
        return self.get_ancestors().type(CaseStudyIndexPage).last()

CaseStudyPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('summary', classname="full"),
    FieldPanel('marketplace_entry', classname="full"),
    MultiFieldPanel(TopImage.panels, "hero image"),
    DocumentChooserPanel('downloadable_package'),
    InlinePanel(CaseStudyPage, 'focus_areas', label="Focus Areas"),
    InlinePanel(CaseStudyPage, 'regions', label="Regions"),
    InlinePanel(CaseStudyPage, 'countries', label="Countries"),
    InlinePanel(CaseStudyPage, 'organizations', label="Organizations"),
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


class RegionCaseStudy(Orderable, models.Model):
    region = models.ForeignKey(Region, related_name="+")
    page = ParentalKey(CaseStudyPage, related_name='regions')
    panels = [
        FieldPanel('region'),
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


# Blog index page


class BlogIndexPage(Page, TopImage):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    subpage_types = ['portal_pages.BlogPage']

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        # Get blogs
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 6)  # Show 6 casestudies per page
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context

BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    MultiFieldPanel(TopImage.panels, "blog image"),
]

BlogIndexPage.promote_panels = Page.promote_panels


# Blog Page


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('portal_pages.BlogPage', related_name='tagged_items')


class BlogPage(Page, TopImage):
    body = RichTextField()
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('body', classname="full"),
    MultiFieldPanel(TopImage.panels, "blog image"),
]

BlogPage.promote_panels = Page.promote_panels + [
    FieldPanel('tags'),
]
