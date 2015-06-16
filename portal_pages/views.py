import random
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MarketplaceEntryPage, MarketplaceIndexPage, Service, Expertise, Country, \
                    Region, ServiceMarketplaceEntry, CountryMarketplaceEntry, RegionMarketplaceEntry, \
                    ExpertiseMarketplaceEntry

from .forms import MarketplaceEntryForm

def get_marketplace_entry(request):
    context = {}
    if request.method == 'POST':
        form = MarketplaceEntryForm(request.POST)
        if form.is_valid():
            marketplace_index = MarketplaceIndexPage.objects.live().first()
            if marketplace_index:
                marketplace_entry_page = form.save(commit = False)
                slug = "marketplace-entry-%d" % random.randrange(100000,999999)
                marketplace_entry_page.slug = slug
                marketplace_entry = marketplace_index.add_child(
                                        instance = (marketplace_entry_page))
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
                return HttpResponseRedirect('/marketplace/')
    else:
        form = MarketplaceEntryForm()

    services = Service.objects.order_by('name')
    expertise_list = Expertise.objects.order_by('name')
    countries = Country.objects.order_by('name')
    regions = Region.objects.order_by('name')
    base_year = datetime.today().year
    years = [base_year - x for x in range(0,100)]
    context = { 'form': form, 'services': services, 'years': years,
                'expertise_list': expertise_list, 'countries': countries,
                'regions': regions}
    
    return render(request, 'portal_pages/markplace_entry_page_add.html', context)