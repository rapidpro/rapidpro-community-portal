# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import modelcluster.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='wagtailcore.Page', serialize=False, primary_key=True, on_delete=django.db.models.deletion.CASCADE)),
                ('home_content', wagtail.core.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageHeroImageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, blank=True, null=True)),
                ('blurb', wagtail.core.fields.RichTextField()),
                ('hero_image', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.CASCADE)),
                ('home_page', modelcluster.fields.ParentalKey(related_name='hero_items', to='portal_pages.HomePage')),
                ('target_page', models.ForeignKey(to='wagtailcore.Page', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
