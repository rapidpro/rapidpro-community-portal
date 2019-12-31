# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0019_auto_20150505_0840'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TechFirm',
        ),
    ]
