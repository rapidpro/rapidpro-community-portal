from django.shortcuts import render
from django.http import HttpResponseRedirect

import random

from .models import Service, MarketplaceEntryPage, MarketplaceIndexPage

def add_marketplace(request):
    services = Service.objects.order_by('name')
    context = {'services': services}
    return render(request, 'portal_pages/markplace_entry_page_add.html', context)

def create_marketplace(request):
    # We might want to look into TestCopyPage
    # Create an unpublished marketplace entry page
    # https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/tests/test_page_model.py
    marketplace_index = MarketplaceIndexPage.objects.get(id=5)  
    
    marketplace_entry = marketplace_index.add_child(
        instance=MarketplaceEntryPage(
            title = request.POST['title'], 
            slug = "marketplace-entry-%d" % random.randrange(100000,999999), 
            date_start = "2015-05-01",
            biography = request.POST['biography']))

    marketplace_entry.unpublish()   

    return HttpResponseRedirect("/marketplace/")
