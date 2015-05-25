from django.shortcuts import render

from .models import Service, MarketplaceEntryPage

def add_marketplace(request):
    services = Service.objects.order_by('name')
    context = {'services': services}
    return render(request, 'portal_pages/markplace_entry_page_add.html', context)

def create_marketplace(request):
    # We might want to look into TestCopyPage
    # Create a simple unpublished page to copy from? Hmm..
    # https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/tests/test_page_model.py
    MarketplaceEntryPage.objects.create(
        title=request.POST['title'],
        date_start='2015-05-01',
        biography=request.POST['biography'],
        depth=4,
        content_type_id=43,
        slug="temp-%s" % request.POST['title']
        )
    return HttpResponseRedirect("add_marketplace")
