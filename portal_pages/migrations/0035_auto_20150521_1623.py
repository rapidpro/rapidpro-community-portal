# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0034_defaulttopimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaulttopimage',
            name='default_top_image',
            field=models.ForeignKey(to='wagtailimages.Image'),
        ),
    ]
