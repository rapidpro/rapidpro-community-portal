# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0020_delete_techfirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudypage',
            name='marketplace_entry',
            field=models.ForeignKey(to='portal_pages.MarketplaceEntryPage', blank=True, null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
    ]
