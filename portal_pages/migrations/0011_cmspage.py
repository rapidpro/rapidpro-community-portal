# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('portal_pages', '0010_remove_casestudypage_feed_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='wagtailcore.Page', parent_link=True, on_delete=django.db.models.deletion.CASCADE)),
                ('body', wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
