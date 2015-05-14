# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0024_auto_20150512_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudypage',
            name='marketplace_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_pages.MarketplaceEntryPage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_case_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_pages.CaseStudyPage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marketplaceentrypage',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_pages.Country'),
            preserve_default=True,
        ),
    ]
