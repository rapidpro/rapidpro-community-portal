from django.shortcuts import render
from django.http import HttpResponseRedirect

import random
from datetime import datetime

from bs4 import BeautifulSoup

from .models import MarketplaceEntryPage, MarketplaceIndexPage, Service, Expertise, Country, Region, ServiceMarketplaceEntry, CountryMarketplaceEntry, RegionMarketplaceEntry, ExpertiseMarketplaceEntry

VALID_TAGS = ['strong', 'em', 'p', 'ol', 'ul', 'li', 'br', 'h2', 'h3', 'h4', 'h5', 'a']

def add_marketplace(request):
    services = Service.objects.order_by('name')
    expertise_list = Expertise.objects.order_by('name')
    countries = Country.objects.order_by('name')
    regions = Region.objects.order_by('name')
    base_year = datetime.today().year
    years = [base_year - x for x in range(0,100)]
    context = {'services': services, 'years': years, 'expertise_list': expertise_list, 'countries': countries, 'regions': regions}
    return render(request, 'portal_pages/markplace_entry_page_add.html', context)

def create_marketplace(request):
    # Create an unpublished marketplace entry page
    # Found source for this on the following file
    # https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/tests/test_page_model.py
    
    marketplace_index = MarketplaceIndexPage.objects.get(id=5)
    
    biography = sanitize_html(request.POST['biography'])
    slug = "marketplace-entry-%d" % random.randrange(100000,999999)

    if request.POST['country']:
        country = Country.objects.get(id=request.POST['country'])
    else:
        country = None

    marketplace_entry = marketplace_index.add_child(
        instance=MarketplaceEntryPage(
            title = request.POST['title'], 
            slug = slug, 
            date_start = request.POST['established']+"-01-01",
            biography = biography,
            telephone = request.POST['telephone'],
            email = request.POST['email'],
            address_1 = request.POST['address_1'],
            address_2 = request.POST['address_2'],
            city = request.POST['city'],
            state = request.POST['state'],
            country = country,
            post_code = request.POST['post_code'],
            website = request.POST['website']
            ))

    if marketplace_entry:

        marketplace_entry.unpublish()

        for service in request.POST.getlist('services'):
            ServiceMarketplaceEntry.objects.create(
                service = Service.objects.get(id=service),
                page = marketplace_entry
            )
        for expertise in request.POST.getlist('expertise'):
            ExpertiseMarketplaceEntry.objects.create(
                expertise = Expertise.objects.get(id=expertise),
                page = marketplace_entry
            )
        for region in request.POST.getlist('regions_experience'):
            RegionMarketplaceEntry.objects.create(
                region = Region.objects.get(id=region),
                page = marketplace_entry
            )
        for country in request.POST.getlist('countries_experience'):
            CountryMarketplaceEntry.objects.create(
                country = Country.objects.get(id=country),
                page = marketplace_entry
            )        

    return HttpResponseRedirect("/marketplace/")

def sanitize_html(value):
    soup = BeautifulSoup(value)

    for tag in soup.findAll(True):
        if tag.name not in VALID_TAGS:
            tag.hidden = True

    return soup.renderContents()
