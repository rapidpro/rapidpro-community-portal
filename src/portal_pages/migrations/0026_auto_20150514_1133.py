# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.fields
from django.db import migrations, models


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
