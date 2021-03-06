# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0013_auto_20150429_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpertiseMarketplaceEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('expertise', models.ForeignKey(to='portal_pages.Expertise', related_name='+', on_delete=django.db.models.deletion.CASCADE)),
                ('page', modelcluster.fields.ParentalKey(to='portal_pages.MarketplaceEntryPage', related_name='expertise_tags')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]
