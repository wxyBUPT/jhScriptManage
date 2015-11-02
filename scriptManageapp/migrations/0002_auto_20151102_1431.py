# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscript',
            name='scriptPath',
            field=models.CharField(max_length=30),
        ),
    ]
