# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('portal_pages', '0015_countrymarketplaceentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketplaceIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True, on_delete=django.db.models.deletion.CASCADE)),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
