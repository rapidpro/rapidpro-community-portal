# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0025_auto_20150518_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketplaceentrypage',
            old_name='branding_banner',
            new_name='top_image',
        ),
    ]
