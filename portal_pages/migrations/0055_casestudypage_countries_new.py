# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0054_cmspage_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudypage',
            name='countries_new',
            field=modelcluster.fields.ParentalManyToManyField(to='portal_pages.Country', blank=True),
        ),
    ]
