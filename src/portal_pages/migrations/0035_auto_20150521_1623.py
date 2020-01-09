# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0034_defaulttopimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaulttopimage',
            name='default_top_image',
            field=models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
