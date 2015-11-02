# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0003_auto_20151102_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pageName',
            new_name='name',
        ),
    ]
