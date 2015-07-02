# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0042_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudyindexpage',
            name='submit_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='casestudyindexpage',
            name='thanks_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
