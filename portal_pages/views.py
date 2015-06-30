from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify

from wagtail.wagtailadmin.utils import send_notification

from .models import (
    Service, Expertise, Country, Region, ServiceMarketplaceEntry,
    CountryMarketplaceEntry, RegionMarketplaceEntry, ExpertiseMarketplaceEntry,
    Tag, BlogPageTag
    )

from .forms import MarketplaceEntryForm, ImageForm, BlogForm


def submit_marketplace_entry(request, marketplace_index):

    form = MarketplaceEntryForm(data=request.POST or None, label_suffix='')

    # If the user uploaded a logo we want the logo_form to validate it is a
    # valid image, but if no logo file was uploaded then proceed with an
    # unbound ImageForm. This avoids re-display due to errors in the main form
    # erroneously telling the user that the logo file is required (it is required
    # for that form, but the entire form is optional).
    if request.FILES:
        logo_form = ImageForm(data=request.POST, files=request.FILES, label_suffix='')
        logo_form_valid = logo_form.is_valid()
    else:
        logo_form = ImageForm(label_suffix='')
        logo_form_valid = True

    if request.method == 'POST' and form.is_valid() and logo_form_valid:
        marketplace_entry_page = form.save(commit=False)
        marketplace_entry_page.slug = slugify(marketplace_entry_page.title)
        marketplace_entry = marketplace_index.add_child(instance=marketplace_entry_page)

        if marketplace_entry:
            if request.FILES:
                logo_image = logo_form.save(commit=False)
                logo_image.title = "Logo for %s" % marketplace_entry_page.title
                logo_image.save()
                marketplace_entry.logo_image = logo_image

            marketplace_entry.unpublish()
            for service in request.POST.getlist('services'):
                ServiceMarketplaceEntry.objects.create(
                    service=Service.objects.get(id=service),
                    page=marketplace_entry
                )
            for service_name in request.POST['services_additional'].split(","):
                service_name = service_name.lstrip().rstrip().capitalize()
                service, created = Service.objects.get_or_create(name=service_name)
                ServiceMarketplaceEntry.objects.create(
                    service=service,
                    page=marketplace_entry
                )
            for expertise in request.POST.getlist('expertise'):
                ExpertiseMarketplaceEntry.objects.create(
                    expertise=Expertise.objects.get(id=expertise),
                    page=marketplace_entry
                )
            for expertise_name in request.POST['expertise_additional'].split(","):
                expertise_name = expertise_name.lstrip().rstrip().capitalize()
                expertise, created = Expertise.objects.get_or_create(name=expertise_name)
                ExpertiseMarketplaceEntry.objects.create(
                    expertise=expertise,
                    page=marketplace_entry
                )
            for region in request.POST.getlist('regions_experience'):
                RegionMarketplaceEntry.objects.create(
                    region=Region.objects.get(id=region),
                    page=marketplace_entry
                )
            for country in request.POST.getlist('countries_experience'):
                CountryMarketplaceEntry.objects.create(
                    country=Country.objects.get(id=country),
                    page=marketplace_entry
                )

            # Submit page for moderation. This reuires first saving a revision.
            marketplace_entry.save_revision(submitted_for_moderation=True)
            # Then send the notification. Last param None means do not exclude any
            # moderators from email (internally wagtail would exclude the user
            # submitting from such emails, be we are submitting something from an
            # anonymous user, so no one should be excluded from the email).
            send_notification(marketplace_entry.get_latest_revision().id, 'submitted', None)
        return HttpResponseRedirect(marketplace_index.url + marketplace_index.reverse_subpage('thanks'))

    services = Service.objects.order_by('name')
    expertise_list = Expertise.objects.order_by('name')
    countries = Country.objects.order_by('name')
    regions = Region.objects.order_by('name')
    base_year = datetime.today().year
    years = [base_year - x for x in range(0, 100)]
    context = {
        'form': form,
        'logo_form': logo_form,
        'services': services,
        'years': years,
        'expertise_list': expertise_list,
        'countries': countries,
        'regions': regions,
        'marketplace_index': marketplace_index,
    }
    return render(request, 'portal_pages/marketplace_entry_page_add.html', context)

def submit_blog(request, blog_index):

    form = BlogForm(data=request.POST or None, label_suffix='')

    if request.method == 'POST' and form.is_valid():
        blog_page = form.save(commit=False)
        blog_page.slug = slugify(blog_page.title)
        blog = blog_index.add_child(instance=blog_page)

        if blog:
            blog.unpublish()

            for tag in request.POST.getlist('tags'):
                BlogPageTag.objects.create(tag=Tag.objects.get(id=tag),
                                           content_object=blog)
            if request.POST['tags_additional']:
                for tag_name in request.POST['tags_additional'].split(","):
                    tag_name = tag_name.lstrip().rstrip()
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    BlogPageTag.objects.create(
                        tag=tag,
                        content_object=blog
                    )

            # Submit page for moderation. This requires first saving a revision.
            blog.save_revision(submitted_for_moderation=True)
            # Then send the notification. Last param None means do not exclude any
            # moderators from email (internally wagtail would exclude the user
            # submitting from such emails, be we are submitting something from an
            # anonymous user, so no one should be excluded from the email).
            send_notification(blog.get_latest_revision().id, 'submitted', None)
        return HttpResponseRedirect(blog_index.url + blog_index.reverse_subpage('thanks'))

    tags = Tag.objects.order_by('name')
    context = {
        'form': form,
        'tags': tags,
        'blog_index': blog_index,
    }
    return render(request, 'portal_pages/blog_page_add.html', context)