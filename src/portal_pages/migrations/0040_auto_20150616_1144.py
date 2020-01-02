# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0039_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceentrypage',
            name='biography',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
