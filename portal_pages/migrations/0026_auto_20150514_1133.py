# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0025_auto_20150514_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmspage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
