# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('portal_pages', '0012_highlightitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketplaceEntryPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, to='wagtailcore.Page', primary_key=True, parent_link=True, on_delete=django.db.models.deletion.CASCADE)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('post_code', models.CharField(blank=True, max_length=10)),
                ('biography', wagtail.core.fields.RichTextField(blank=True)),
                ('date_start', models.DateField(verbose_name='Company Start Date')),
                ('branding_banner', models.ForeignKey(null=True, blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL)),
                ('country', models.ForeignKey(to='portal_pages.Country', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceMarketplaceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='services', to='portal_pages.MarketplaceEntryPage')),
                ('service', models.ForeignKey(related_name='+', to='portal_pages.Service', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='date',
            field=models.DateField(verbose_name='Create date'),
            preserve_default=True,
        ),
    ]
