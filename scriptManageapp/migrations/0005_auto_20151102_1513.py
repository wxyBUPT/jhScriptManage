# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0004_auto_20151102_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='proName',
            new_name='name',
        ),
        migrations.AddField(
            model_name='page',
            name='developers',
            field=models.ManyToManyField(to='scriptManageapp.Developer'),
        ),
    ]
