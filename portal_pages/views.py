from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify

from wagtail.wagtailadmin.utils import send_notification

from .models import (
    Service, Expertise, Country, Region, ServiceMarketplaceEntry,
    CountryMarketplaceEntry, RegionMarketplaceEntry, ExpertiseMarketplaceEntry,
    CountryCaseStudy, RegionCaseStudy, FocusAreaCaseStudy, OrganizationCaseStudy,
    FocusArea, Organization
    )

from .forms import MarketplaceEntryForm, CaseStudyForm, DocumentForm


def submit_marketplace_entry(request, marketplace_index):
    form = MarketplaceEntryForm(data=request.POST or None, label_suffix='')
    if request.method == 'POST' and form.is_valid():
        marketplace_entry_page = form.save(commit=False)
        marketplace_entry_page.slug = slugify(marketplace_entry_page.title)
        marketplace_entry = marketplace_index.add_child(instance=marketplace_entry_page)

        if marketplace_entry:
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
        'services': services,
        'years': years,
        'expertise_list': expertise_list,
        'countries': countries,
        'regions': regions,
        'marketplace_index': marketplace_index,
    }
    return render(request, 'portal_pages/marketplace_entry_page_add.html', context)

def submit_case_study(request, case_study_index):
    form = CaseStudyForm(data=request.POST or None, label_suffix='')
    if request.method == 'POST' and form.is_valid():
        case_study_page = form.save(commit=False)
        case_study_page.slug = slugify(case_study_page.title)
        case_study = case_study_index.add_child(instance=case_study_page)

        if case_study:
            case_study.unpublish()
            for focus_area in request.POST.getlist('focus_areas'):
                FocusAreaCaseStudy.objects.create(
                    focusarea=FocusArea.objects.get(id=focus_area),
                    page=case_study
                )
            for focus_area_name in request.POST['focus_areas_additional'].split(","):
                focus_area_name = focus_area_name.lstrip().rstrip().capitalize()
                focus_area, created = FocusArea.objects.get_or_create(name=focus_area_name)
                FocusAreaCaseStudy.objects.create(
                    focusarea=FocusArea.objects.get(id=focus_area),
                    page=case_study
                )
            for region in request.POST.getlist('regions_experience'):
                RegionMarketplaceEntry.objects.create(
                    region=Region.objects.get(id=region),
                    page=case_study
                )
            for country in request.POST.getlist('countries_experience'):
                CountryMarketplaceEntry.objects.create(
                    country=Country.objects.get(id=country),
                    page=case_study
                )

            # Submit page for moderation. This reuires first saving a revision.
            case_study.save_revision(submitted_for_moderation=True)
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
        'services': services,
        'years': years,
        'expertise_list': expertise_list,
        'countries': countries,
        'regions': regions,
        'marketplace_index': marketplace_index,
    }
    return render(request, 'portal_pages/marketplace_entry_page_add.html', context)

