# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0020_delete_techfirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudypage',
            name='marketplace_entry',
            field=models.ForeignKey(related_name='+', to='portal_pages.MarketplaceEntryPage', default=1),
            preserve_default=False,
        ),
    ]
