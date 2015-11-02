# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0005_auto_20151102_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='testscript',
            name='testPage',
            field=models.ManyToManyField(to='scriptManageapp.Page'),
        ),
    ]
