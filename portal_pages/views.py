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
    
    biography = format_biography(request.POST['biography'])
    
    marketplace_entry = marketplace_index.add_child(
        instance=MarketplaceEntryPage(
            title = request.POST['title'], 
            slug = "marketplace-entry-%d" % random.randrange(100000,999999), 
            date_start = "2015-05-01",
            biography = biography))

    marketplace_entry.unpublish()   

    return HttpResponseRedirect("/marketplace/")

def format_biography(biography):
    # String comes through with hallojs formatting
    # Reformat them with <h1>, <h2> and <h3>, <b> and <i>, and <ul><li>

    biography_formatted = biography

    # Need to find a utility that turns markdown into html
    
    while(biography_formatted.find("### ") >= 0):                                             
        h3_begin = biography_formatted.find("### ")
        h3_end = biography_formatted.find("\r\n\r\n", h3_begin)
        biography_formatted = biography_formatted[0:h3_begin] + "<h3>" + biography_formatted[h3_begin+4:h3_end] + "</h3>" + biography_formatted[h3_end+4:len(biography_formatted)]

    while(biography_formatted.find("## ") >= 0):                                             
        h2_begin = biography_formatted.find("## ")
        h2_end = biography_formatted.find("\r\n\r\n", h2_begin)
        biography_formatted = biography_formatted[0:h2_begin] + "<h2>" + biography_formatted[h2_begin+3:h2_end] + "</h2>" + biography_formatted[h2_end+4:len(biography_formatted)]

    while(biography_formatted.find("# ") >= 0):                                             
        h1_begin = biography_formatted.find("# ")
        h1_end = biography_formatted.find("\r\n\r\n", h1_begin)
        biography_formatted = biography_formatted[0:h1_begin] + "<h1>" + biography_formatted[h1_begin+2:h1_end] + "</h1>" + biography_formatted[h1_end+4:len(biography_formatted)]
    
    # while(biography_formatted.find("**") >= 0):                                             
    #    biography_formatted = biography_formatted.replace("**", "<b>")
    """
    while(biography_formatted.find("_") >= 0):                                             
        i_begin = biography_formatted.find("_")
        i_end = biography_formatted.find("_", i_begin+1)
        biography_formatted = biography_formatted[0:i_begin] + "<i>" + biography_formatted[i_begin+1:i_end] + "</i>" + biography_formatted[i_end+4:len(biography_formatted)]
    """

    biography_formatted = biography_formatted.replace("*   ", "</ul></li><ul><li>")

    biography_formatted = biography_formatted.replace("\r\n", "") # Strip out any remaining carriage returns

    return biography_formatted
