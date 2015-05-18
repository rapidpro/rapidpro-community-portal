# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('portal_pages', '0027_casestudyindexpage_top_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceindexpage',
            name='top_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
    ]
