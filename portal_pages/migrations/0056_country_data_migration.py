# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


# Loop through all Case Study pages and save the countries
# to the new ParentalManyToManyField

def no_op(apps, schema_editor):
    # Do nothing on reversal to data
    pass

def save_countries_to_new_parental_m2m(apps, schema_editor):
    # Need to import the actual model here
    # versus the "fake" model
    # so that the Clusterable model logic works and we can
    # successfully save the ParentalManyToManyField

    from portal_pages.models import CaseStudyPage

    for csp in CaseStudyPage.objects.all():
        csp.countries_new = [country.country for country in csp.countries.all()]
        csp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0055_casestudypage_countries_new'),
        ('wagtailcore', '0038_make_first_published_at_editable')
    ]

    operations = [
        migrations.RunPython(save_countries_to_new_parental_m2m, no_op),
    ]
