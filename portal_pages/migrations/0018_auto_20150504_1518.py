# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def no_op(apps, schema_editor):
    # Do nothing on reversal
    pass


def create_focus_areas(apps, schema_editor):
    FocusArea = apps.get_model('portal_pages', 'FocusArea')
    fa_names = [
        'Education',
        'Health',
        'Engagement',
        'Program Monitoring',
    ]
    for fa_name in fa_names:
        FocusArea.objects.get_or_create(name=fa_name)


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0017_auto_20150504_1517'),
    ]

    operations = [
        migrations.RunPython(create_focus_areas, no_op),
    ]
