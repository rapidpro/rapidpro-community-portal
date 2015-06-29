# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0039_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceentrypage',
            name='biography',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]
