# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import modelcluster.fields
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('portal_pages', '0011_cmspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(editable=False, blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('blurb', wagtail.core.fields.RichTextField()),
                ('home_page', modelcluster.fields.ParentalKey(to='portal_pages.HomePage', related_name='highlights')),
                ('icon', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.CASCADE)),
                ('target_page', models.ForeignKey(to='wagtailcore.Page', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
