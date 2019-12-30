# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('portal_pages', '0042_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceentrypage',
            name='logo_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizationcasestudy',
            name='organization',
            field=models.ForeignKey(to='portal_pages.Organization', related_name='+', verbose_name='organisation', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
