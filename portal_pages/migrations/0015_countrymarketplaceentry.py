# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0014_expertise_expertisemarketplaceentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryMarketplaceEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('country', models.ForeignKey(related_name='+', to='portal_pages.Country')),
                ('page', modelcluster.fields.ParentalKey(related_name='countries', to='portal_pages.MarketplaceEntryPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]
