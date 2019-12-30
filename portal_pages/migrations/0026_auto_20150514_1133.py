# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0025_auto_20150514_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmspage',
            name='body',
            field=wagtail.core.fields.RichTextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
