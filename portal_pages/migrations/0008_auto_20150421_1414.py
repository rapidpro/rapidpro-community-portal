# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('portal_pages', '0007_casestudydownloadablepackage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudyheroimageitem',
            name='casestudy_page',
        ),
        migrations.RemoveField(
            model_name='casestudyheroimageitem',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='casestudyheroimageitem',
            name='target_page',
        ),
        migrations.DeleteModel(
            name='CaseStudyHeroImageItem',
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
    ]
