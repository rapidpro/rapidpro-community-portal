# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0040_auto_20150616_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceindexpage',
            name='submit_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='marketplaceindexpage',
            name='thanks_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
